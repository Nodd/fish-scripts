function yU -d "Update all packages using yaourt or apt-get"
	if which yaourt
		yaourt -Sauy
	else;
        sudo apt-get update
        sudo apt-get upgrade
    end
end
