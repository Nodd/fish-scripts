function yS -d "Install a package using yaourt or apt-get"
    if which yaourt
		yaourt -S $argv
	else;
        sudo apt-get install $argv
    end
end
