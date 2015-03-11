set --erase fish_greeting

for dir in /usr/local/anaconda/bin ~/bin ~/.bin
    if [ -d $dir ]
        set PATH $dir $PATH
    end
end

# start X at login
#if status --is-login
#    if test -z "$DISPLAY" -a $XDG_VTNR = 1
#        exec startx
#    end
#end
