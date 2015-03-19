set --erase fish_greeting

for dir in /usr/local/bin /usr/local/anaconda/bin ~/bin ~/.bin
    if [ -d $dir ]
        set PATH $dir $PATH
    end
end

alias lt "ls -lrt"

for host in (~/.config/fish/hosts.py)
    alias $host "ssh -YC $host"
end


# start X at login
#if status --is-login
#    if test -z "$DISPLAY" -a $XDG_VTNR = 1
#        exec startx
#    end
#end
