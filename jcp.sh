#!/usr/bin/env bash

jcp-tune() {
  subl ~/bin/get-jcp.py
  subl ~/bin/jcp.sh
  subl ~/bin/jcp.yaml
  echo "Open files at Sublime Text for edit"
  echo "Please run these commands after:"
  echo "python3 ~/bin/get-jcp.py"
  echo "source ~/.zshrc"
}

jcp-regen() {
  python3 ~/bin/get-jcp.py
  source ~/.zshrc
}

home() {
  cd /Users/dmytro || return
  echo "Here is my home dir"
}

j() {
    if [ $# -eq 1 ]; then
        choice=$1
    else
        echo 'Select a project:'
        echo '0. jcp-tune'
        echo '1. jcp-regen'
        echo '2. home'
        read -r choice
    fi
    clear
    case $choice in
      0) jcp-tune ;;
      1) jcp-regen ;;
      2) home ;;
      jcp-tune) jcp-tune ;;
      jcp-regen) jcp-regen ;;
      home) home ;;
      *) echo 'Invalid selection' ;;
    esac
}
