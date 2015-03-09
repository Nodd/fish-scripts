function yS -d "Install a package using yaourt or apt-get"
    if which yaourt > /dev/null
        yaourt -S --needed $argv
    else
        sudo apt-get install $argv
    end
end
