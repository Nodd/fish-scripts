function ys -d "search a package using yaourt or apt-cache"
    if which yaourt > /dev/null
            yaourt -Ss $argv
    else
        apt-cache search $argv
    end
end
