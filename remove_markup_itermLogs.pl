#!/usr/bin/perl
#remove_markup_itermLogs.pl
#execute the script by running ..
#./remove_markup_itermLogs.pl <file_name> > <output_filename>

while (<>) {
    s/ \e[ #%()*+\-.\/]. |
       \r | # Remove extra carriage returns also
       (?:\e\[|\x9b) [ -?]* [@-~] | # CSI ... Cmd
       (?:\e\]|\x9d) .*? (?:\e\\|[\a\x9c]) | # OSC ... (ST|BEL)
       (?:\e[P^_]|[\x90\x9e\x9f]) .*? (?:\e\\|\x9c) | # (DCS|PM|APC) ... ST
       \e.|[\x80-\x9f] //xg;
       1 while s/[^\b][\b]//g;  # remove all non-backspace followed by backspace
    print;
}
