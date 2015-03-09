function yR -d "Remove a package using yaourt or apt-get"
    if which yaourt > /dev/null
            yaourt -Rcs $argv
    else
        sudo apt-get remove $argv
    end
end
