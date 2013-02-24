set term pdfcairo color transparent size 4in, 3in

set xtics rotate by 0 font ",5" nomirror
set ytics nomirror
set key font ",5"
set tic font ",5"

set style fill solid 0.7 border rgb "black"
set style data histogram
set style histogram cluster gap 1
set bmargin 5
set ylabel "time (s)"
set boxwidth 1

set style line 12 lc rgb "#ddccdd" lt 1 lw 1.0
set style line 13 lc rgb "#ddccdd" lt 0 lw 1.0
set grid ytics mytics back ls 12, ls 13

dir = "times/"
firstColor = "#8c8c8c"
secondColor = "#fca311"
f(x) = (x < 100 ? 1/0 : x < 200 ? 90 : 90)

set title "WORDS"
set output "english.pdf"
set yrange [0:100]
set ytics 20
set mytics 4
plot dir . "words.times" using 2:xtic(1) title "100MB" with histogram lc rgb firstColor,\
     "" using 3:xtic(1) title "200MB" with histogram lc rgb secondColor,\
     "" using (column(0) - 0.6):(f($2)):2 with labels font ",5" rotate by 0 title "",\
     "" using (column(0) + 0.6):(f($3)):3 with labels font ",5" rotate by 0 title ""

set title "DNA"
set output "dna.pdf"
#set key left
set yrange [0:2.5]
set ytics 0.5
set mytics 5
plot dir . "dna.times" using 2:xtic(1) title "100MB" with histogram lc rgb firstColor,\
     "" using 3:xtic(1) title "200MB" with histogram lc rgb secondColor

set title "PROTEINS"
set output "proteins.pdf"
set yrange [0:25]
set ytics 5
set mytics 5
plot dir . "proteins.times" using 2:xtic(1) title "100MB" with histogram lc rgb firstColor,\
     "" using 3:xtic(1) title "200MB" with histogram lc rgb secondColor

set title "URLS"
set output "urls.pdf"
set yrange [0:70]
set ytics 20
set mytics 4
plot dir . "urls.times" using 2:xtic(1) title "100MB" with histogram lc rgb firstColor,\
     "" using 3:xtic(1) title "200MB" with histogram lc rgb secondColor
