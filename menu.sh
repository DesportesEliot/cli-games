#!/bin/bash

select_option() {
    clear
    local -r ESC=$(printf "\033")
    local -a options=("$@")
    local selected=1
    local prompt="$1"
    local last_index=$((${#options[@]} - 1))
    local input=""

    cursor_blink_on()   { printf "$ESC[?25h"; }
    cursor_blink_off()  { printf "$ESC[?25l"; }
    cursor_to()         { printf "$ESC[$1;${2:-1}H"; }
    print_option()      { printf "    %s\n" "$1"; }
    print_selected()    { printf "$ESC[34m  ⤷ $ESC[4m%s$ESC[0m\n" "$1"; }
    clear_line()        { printf "$ESC[2K"; }
    print_input()       { printf "  Search: %s\n" "$input"; }

    # Function to normalize text (remove accents and convert to lowercase)
    normalize_text() {
        echo "$1" | tr '[:upper:]' '[:lower:]' | iconv -f utf-8 -t ascii//TRANSLIT
    }

    # Function to find the first match
    find_match() {
        local search="$1"
        local normalized_search
        local normalized_option
        local i
        local found=false
        
        normalized_search=$(normalize_text "$search")
        
        for i in "${!options[@]}"; do
            normalized_option=$(normalize_text "${options[i]}")
            if [[ "$normalized_option" =~ ^"$normalized_search" ]]; then
                selected=$i
                found=true
                break
            fi
        done
        
        if [ "$found" = false ]; then
            # Keep only the last character
            input="${input: -1}"
            # If input is empty after keeping last char, try to find a match with it
            if [ -n "$input" ]; then
                normalized_search=$(normalize_text "$input")
                for i in "${!options[@]}"; do
                    normalized_option=$(normalize_text "${options[i]}")
                    if [[ "$normalized_option" =~ ^"$normalized_search" ]]; then
                        selected=$i
                        found=true
                        break
                    fi
                done
            fi
        fi
    }

    trap "cursor_blink_on; stty echo; printf '\n'; exit" SIGINT

    cursor_blink_off
    stty -echo

    cursor_to 0
    clear_line
    printf "$prompt"

    while true; do
        for i in "${!options[@]}"; do
            if (( i == 0 )); then
                continue
            fi

            cursor_to $((i + 1))
            clear_line
            if [[ $i == $selected ]]; then
                print_selected "${options[i]}"
            else
                print_option "${options[i]}"
            fi
        done

        # Print input line
        cursor_to $((last_index + 2))
        clear_line

        # Print help message
        cursor_to $((last_index + 3))
        clear_line
        printf "  \033[2m↑/↓: Navigate | Type to search | Enter: Select | Ctrl+C: Quit\033[0m\n"

        # read user key
        IFS= read -rsn1 key  # Read first character
        if [[ $key == $ESC ]]; then
            read -rsn2 key  # Read 2 more chars
            if [[ $key == "[A" ]]; then  # Up
                ((selected--))
                ((selected < 1)) && selected=$last_index
            elif [[ $key == "[B" ]]; then  # Down
                ((selected++))
                ((selected > $last_index)) && selected=1
            fi
        elif [[ $key == "" ]]; then  # Enter
            break
        elif [[ $key == $'\x7f' ]]; then  # Backspace
            input="${input%?}"
            find_match "$input"
        else  # Regular character
            input+="$key"
            find_match "$input"
        fi
    done

    cursor_to $((last_index + 2))
    cursor_blink_on
    stty echo
    printf "\nYou selected: %s\n" "${options[selected]}"
    return $(( selected - 1 ))
}

get_game_directories() {
    # Find all directories that don't start with "_" and store them in an array
    local game_dirs=()
    while IFS= read -r dir; do
        game_dirs+=("$dir")
    done < <(find . -maxdepth 1 -type d -not -path "*/\.*" -not -path "*/_*" -not -path "." -not -path "*/venv" | sed 's|^\./||' | sort)
    echo "${game_dirs[@]}"
}

check_game_files() {
    if command -v deno &>/dev/null; then
		jsCmd="deno run"
	elif command -v node &>/dev/null; then
		jsCmd="node"
	else
		echo "Neither deno nor node is installed. Please install one of them."
		exit 1
	fi

	local game_dir="$1"
    local has_python=false
    local has_js=false

    if [ -f "$game_dir/__init__.py" ]; then
        has_python=true
    fi
    if [ -f "$game_dir/index.js" ]; then
        has_js=true
    fi

    local game_command=""
    if [ "$has_python" = true ] && [ "$has_js" = true ]; then
        local versions=("Python" "JavaScript")
        select_option "Both Python and Node.js versions are available. Which one would you like to run?" "${versions[@]}"
        local version_choice=$?
        if [ $version_choice -eq 0 ]; then
            echo "Running Python version..."
            game_command="cd "$game_dir" && python3 __init__.py"
        else
            echo "Running JavaScript version..."
            game_command="cd "$game_dir" && $jsCmd index.js"
        fi
    elif [ "$has_python" = true ]; then
        echo "Running Python version..."
        game_command="cd "$game_dir" && python3 __init__.py"
    elif [ "$has_js" = true ]; then
        echo "Running JavaScript version..."
        game_command="cd "$game_dir" && $jsCmd index.js"
    else
        echo "Error: No game files found in $game_dir"
        exit 1
    fi
    eval "$game_command"
    handle_replay "$game_command"
}

handle_replay() {
    local game_command="$1"
    local replay_options=("Yes" "Go back to menu" "Quit")
    select_option "Replay?" "${replay_options[@]}"
    local option=$?
    
    if [[ $option -eq 0 ]]; then
        cd ..
        eval "$game_command"
        handle_replay "$game_command"
    elif [[ $option -eq 1 ]]; then
        cd ..
        show_menu
    else
        exit
    fi

}

function show_menu() {

    # Get game directories and add Quit option
    game_dirs=($(get_game_directories))
    options=("${game_dirs[@]}" "Quit")
    select_option "Select a game" "${options[@]}"
    selected_index=$?

    # Handle the selection
    if [ $selected_index -eq ${#game_dirs[@]} ]; then
        echo "▄▄▄▄·  ▄· ▄▌▄▄▄ .      " | lolcat -s 10000
        echo "▐█ ▀█▪▐█▪██▌▀▄.▀·      " | lolcat -s 10000
        echo "▐█▀▀█▄▐█▌▐█▪▐▀▀▪▄      " | lolcat -s 10000
        echo "██▄▪▐█ ▐█▀·.▐█▄▄▌      " | lolcat -s 10000
        echo "·▀▀▀▀   ▀ •  ▀▀▀  ▀  ▀ " | lolcat -s 10000
        exit 0 
    else
        selected_game="${game_dirs[$selected_index]}"
        check_game_files "$selected_game"
    fi
}

show_menu