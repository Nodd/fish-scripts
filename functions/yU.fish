function yU -d "Update all packages using yaourt or apt-get"
    if which yaourt > /dev/null
            yaourt -Sauy --devel --noconfirm --needed
    else
        sudo apt-get update
        sudo apt-get upgrade
    end
end
