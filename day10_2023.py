# %%

input = """
F|--L7J.L7|7|-LF7-7--7F7--7F7J--F7J.7F|J7.F7|.-FJF|J.F7F--LFF.7.F7JFL-JFJ7F|.FL77-F7-J.F7-F7L-FF-F-L7F-|7.FL7-7F|7F7.F-F|-77FJ7FF-J777.|FFFL
FJJ7FJ.F.-7-|77|JFJJL|7|F7-FJ7JLL|||L-L7-FJJ|7.|J-.J..LJ.--F|7F-FJ7|LJJF7L7J.|-7.FL|.L--7-L|JFL-F|7L|7-|F7F|7.LJ.F7.|L7L-J|-|-LFF-LLJ|LL7|7J
F|.FL|.LJ-L.||FL-|-FJ|JJ7-7|.J.F7--F-|-|FJ-|-|7.|.7|F7.|-L-LJFL--77.F-|J|F-7F--JLJ7|..LLJ.LLJL7JLJ7-F-F7|FJL-77.FJJFL-|F|7F-F7F7JF-77||JLJLJ
||FJ|LF-7F|F|LJFFL-|F|7|JF-J7LJF7.|L-J.F|J7||FJ.LJL-|J.|.F-7F7J.F-|7F-J7L7-77L||L7F7FF7-|JLF-.7-F|-7LLJ7F-.LFJ77L|.|.|L|.L--|JFF7F7L|L|||.LF
L-L-|..J-J|7.|J-||LFF--7-J.|7|.FJ-L7.LFJ|LF7.||.|.F---FF77|F||7-7J|7|LF-L.|FJLF|L||LJFL.|LF-L|L-JFFJ.FLJ-JFJ|L---|-7-F-|7LF-J-JF-JF-.||LJ.|.
J..||FJJFLL--JF7|J.LF7.|JLFJLL7||.JJ7F--J-|L-|FLLF77|-F|L77F||7-|.|FF7J|JF7J|FJ7-FL7.|.FJFFJ7|7J-LF7-F77LF|L7J7LF77L-J.L--7JJ.FL7JF--7-L|7L7
L|--FFJ7F|JJJF-|J.F7.FF7-F77LFF-F-L7F7777L|.L.F77|L7F-7L7|7FJL7F77LF||77F-LF7-FL77-LF77.|7.L|LFF-FJ|F7JJFF.FL-J.LJ|7JFFFLF...FJ.JL77--JFF|.J
F7-F-.|-77JF-F|||7.LF-J-.F|777.FJF.FJ|7-J-J7..F7FJFJL7|FJL7|F7LJL7F-JL7F7..7|FF---7L|L7F7-F-|-F7FL7|||7-J|FF|.J-F-JFJFFJL--77JLFJFJ77.-7.-.L
J--F7.7.||F||.7-7||.L7JF-FJL-JFF-|7L7L7.L|JF-F|LJFJ.F||L-7|LJ|F--JL7F-J||F7.7-L--7L-JFJ||F7FFFJL7FJLJ|7JL-7-F7.-FJFL7F--7.FL-.F|F|||LJF|7LF|
|JLL77.FLJJLL-JLLL77|LFL7F7LLLJ..||.|FJ7-F7LF|L-7|F7FJ|F7|L7-|L7F7FJL7FJ|||F7F--7L--7L7|LJL7FJF-JL-7FJ777L||||7|F-7|L7JLF7FFLLF-7LFJ|LJL|L--
-7F-.7-F||.FFJ7..L77J.F7F7..LLJF77LFJL77|LJ7-F7FJ|||L7|||L7|FJFJ||L7FJL7|||||L-7|F7.|FJL7F-JL7|-F7F|L-7F7F7FJL-7|FJJLF.LL7-LF-F-7L--7F|.LJ.J
LF-7|JFJ|J-F|7FF77L||--|L|7..|.FLJFL7FJJFF.F7||L7LJL7|||L7||L7L7|L7|L--JLJ||L7||||L7|L-7|L--7|L7|L7|F-J||||L7F-J||7.F|7-FL.LJ-|7J|LJL777..-7
||.J---|JJF7-L-|7--F-7F|.|JL.|7J|L7FJL-7-JFJLJL-JF7FJ|LJFJ|L7|FJL7||F---7FJL7L7|||FJ|F-J|F--J|FJL7|||F7|||L7||F7|L77--|.--7F|-|J-L.7-LJ7F--|
LLFJF77FJ.-JJ..L|JL.L77-LJ.LJL|FL.FL-7FJLFJF---7FJLJFJF-JJL7||L7J|||L--7LJ||L7|||||FJL--JL7F7||F7||||||||L7||||||FJ-F7|F|L|77LLJ-|FF-LJL|J7|
F-|F-7-J.-|J|.|.|..F-||7L-FJ|FF|7F---JL-7L-JF--JL7F7|FJF---JLJFJFJLJF--JF-7F7|||||LJF-7F--J|||||||||LJ||L7|||||||L---77F|JF-7-FJ.FJ.7.J|LJF.
7FJ7F|..-.|F77|F|7.L-FF-7.|-|F--7L----7FJF-7L-7F7LJ||||L-----7L7L7F-JF7FL7|||||||L7FJ.LJF-7||||||||L-7|L7||||||LJF7F-JF77.||77|JFLJ.L.LFJ7LF
|77|-F-7L7.|.LF-J-.F-7J.F777FL-7|F7|F7|L7L7L7LLJL-7||L7F-7LF7L7L7|L--JL7||||LJ||L7|L-7F7|FJ|||LJ|||F-JL7|||LJLJF-JLJF7||F7-LFFJF|J-F|-7||JFL
|-L.F|.L7F-J7JJLJL-|.|-F|L7F77FJ|||FJ|L7L7L7|F7F-7||L7||FJFJL7|FJ|F---7L7||L-7|L7LJF-J||||F|||F7LJ|L--7|||L7F7FJFF7-||||||F--7--LJF|--LF--LJ
L7|-FJ--77JFL--.7-L|-7-F|FJF-7L7|||L7L7|FJFJLJ|L7|||FJLJL7L-7||L-JL--7|FJ|L7FJ|L|F7|F-J||L-J|LJ|F-JF7FJ|||FJ|LJF7||FJLJ||||F-J..LF|.|L7JF|F.
|FF-LJJFJ|7J.LLF7JL|-|FJ|L7L7L7|||L7L7||L7L-7FJFJLJ|L7F--JF-J||F-----JLJFL7|L7|FJ|LJL-7||F--JF7||F7||L7LJLJFJF-JLJLJF-7LJLJL7F-7FL|F7-7LF-|7
7LL7|.777LJFL7|||7F7--J.L7L-JFJ||L7L-J|L7|JFJL7L--7L7||.F7L-7|||F7FF--7F--J|FJ|L7L-7F7|LJ|F7L|||||LJ|FJF-7FJL|F---7FJFJF7F-7|JFFL-7-|J|FJ7F7
-7LFFJL|7J7J|-F|L-JL7|.FLL--7L-J|FJF--J|||FJF-JF7JL7LJ|FJ|F-JLJ||L-JF-JL--7|L7|F|F-J|||F7LJL7|||LJF-JL-JFJL7FJL7F7LJ|L7||L7LJF-F.|J.L7LJ||.|
LF-7J.FLJ7J-FJLL7F--J7FF7JF7L--7|L7|7F7FJ|L7|F7|L7LL7FJ|FJL-7F7LJF7FJ|F7.FJL-J|FJL77||LJL-7FJ|||F-JF7F77L-7||F7||L7F7JLJL-JJ.---77.-|-|FL-L7
FLJ|JFJJ||7.L7F-JL-7LF-JL-J|F7|||-|L7|||FJFJ|||L7L7FJL-J|F7-||L-7|LJF7|L7L---7LJF-JFJL7F7J|L7||||F7||||F7FJLJ|LJ|FJ|L-7F7F7777|L|7J|JLJFJ..F
77JL.J7FLFLLJLL---7L7L7F--7|||FJ|FJFJ||||JL7LJL7|FJL-7F7|||FJL-7|L7F|||FJF--7L-7|F7|F-J||FJFJ|||||||LJLJ|L-7FJF7||L|F-J|LJL-7-F|.|-J7F---F-|
L7|7LJL7|F.L7|L-F-JFJ7||F-JLJLJFJL7L-J||L7|L--7||L7F7LJ|LJ||F-7|L-JFJLJL7L7FJF-J||LJ|F7||L7|-||||||L---7L7FJL7||||FJ|F7|F---JLF.LJJJ|FL|7|J|
-77JF-JLL7-JL7|.L-7L-7LJL-----7|F7L--7||FJF---JLJFJ|L7-L7FJ|L7||F7FJF-7FJFJL7L-7LJF7||||L7||FJ|||||-F7FJFJL7FJ|||||FJ|||L--7|..L|7---7LL-F.7
FF|.-77-F-7FL|7-F-JF7L77-F7-F7||||F7FJLJL7|F--7F7L7L7|F7|L-JFJLJ||L-JFJ|FJF7L7FJF7|LJ||L7||LJFJ|LJ|FJLJFJ7FJL-JLJLJL-JLJF-7L-7..|LJ|FL-J-|7L
FJJ-L|-F|J7L.F--JF7|L7L7FJL-JLJLJ|||L--7FJLJF7||L-JJ|||||F-7L-7FJL--7L7|L-JL7||FJLJF-JL-JLJF-JLL-7|L--7L--JF------7F----J|L--J7-L.77FL.|7|-7
FJ7|FLJ||.LJ-L---JLJFJFJ|F7F7F--7LJ|FF-JL-7FJLJ|FF7FJ||LJL7|F-JL7F--JFJ|F7F7|LJL-7|L-----7FJF7F7FJ|F7FJF7F7L-7F--7LJF----7F7F7F77.7-F.FF7J-J
J7-F7-F|7.||F|J|F--7L7L7LJLJLJF7L-7L7L--7FJL--7L7||L7|L-7FJLJFF7||7F7L7||||||F--7L7F-7F-7|L7|||LJFJ||L7|LJL-7LJF-JF-JF---J||||||F77-J7F7||7.
|J-LJF|JL-L-JLLLL-7|7L7|-F7FSFJL7FJFJF7FJL---7L7LJ|FJ|F7|L7F-7|||L7|L7|||||LJ|F7L-JL7||FJ|FJ||L-7L7|L7|L7F7FJF7|F7L-7L7F7F|||LJ||L77JJFL-7FJ
L-7|.|..|LJ|L-||FFJL--J|FJ||LJF7|L7|7|LJF----J|L7FJL7||||FJ|FJ|||FJL7||||||F-J||F7F7||||FJ|F||F7L7|L7||FJ||L-J|LJL--JFJ||FJLJF7LJFJ77FL|J|J.
L-F--J7F|-J|7.-F-JF7F-7|L7|L--J||FJL7L-7|F7F7F-7||F7||||||FJ|FJ||L7FJ||||||L7FJ||||LJ||||FJFJ|||FJ|FJ||L7|L--7|F7F---J-|LJF7FJL--JL777F-JL-J
LLF-L7FJLL7JF7LL7FJLJFJL-JL--7FJLJF7|F7|||||||FJ||||||||||L7|L7|L7|L7||||||FJ|FJ||L-7|||||L|FJ||L7|L7||FJ|F--JLJ|L77F--JF7||L7F7F7F7F-7LF|7|
F7.L7L7J.77-||F7LJF7FJF7F7F7FJL--7|||||||||||||FJ||||LJ|||FJL7||FJ|FJ||||LJL7||FJ|F7|||LJ|FJL7|L7||FJ|||FJL-7F7.L7L-JF-7|LJL-J|||||LJFJ7LL7J
|77.J7L-7|FJ|||L--JLJFJLJLJ||FF7LLJ|||||||||LJ||FJ||L-7|||L-7||LJ||L7||||F-7|||L7||||LJF-J|F7||FLJ||FJ|||F--J|L-7L---JJLJJF-7L|||||F-JJL-J|7
L7---LJ-J-F-J|L-----7|F---7|L-JL---JLJLJLJ|L-7||L7|L7FJ|||F7|LJF--JFJLJLJL7LJ|L7||||L-7|F7||LJL-7FJ|L7|LJL--7|F-JF-7F77F-7L7L-JLJLJL7.|L7J-|
.7JJ7||LLLL-7L7LF7F7LJL--7LJF7F-7F-------7|F7||L7||FJ|FJ|||||F7L--7L---7F-JF7L7||LJL7FJ||||L7F-7|L-JJLJF--7FJ||F-JFJ|L7|FJFJF7F7F-7FJF--77J|
FJ.FJ7L7.L|-L7L7|||L7F7F7L7FJ||7LJJF-7F-7|LJLJL7|||L7|L-J|||||L---JF---JL-7||FJLJF--JL7||||FJ|.|L7F---7L-7LJL||L-7L-JFJ|L-JFJ||||FJL-JF-J-F.
|.FLLL.FFFJ.|L7|||L7LJLJL7||JLJF---JJ|L7|L---7FJ||L7|L7F-J|LJL--7F7L-----7|||L--7L7F-7|LJ||L7L7|FJ|F-7L--JJF7||F7|F--JF|F7FJ.LJLJL7F--J7..LL
F.7F|L7L7|F7F7||||FJF-7F7LJ|F--JF---7|FJ|F7F-JL7||FJL7|L-7L7F---J||F---7FJ|||F7FJFJ|FJL7FJ|FJFJ||LLJFJF---7|||||LJL----J||L--7F7F-JL-7F7J7-|
L-L-7L--JFJLJLJLJLJFJ|LJL-7|L---JF--JLJJLJLJF7JLJ|L-7LJF7|FJ|F7F7|||F-7LJFJ|||||7L7|L7FJ|FJ|FJFJ|F--JFJF--J|||LJF7F-----JL---J||L7F7FJ||LF-J
LFF7FJ||-L-----7F7FJF-7F7FJ|F--7JL---------7||F--JF7|F-JLJ||||||LJ|LJFJ|FJFJ|||L-7|L7|L7LJFJ|||FJL---JLL---JLJF-J|L--------7F-JL7|||L-J|-J7|
-J|FLJF7LLJF---J||L7L7LJLJFJL-7L7F7F----7F7LJ|L7F7|||L7F-7L7LJ||F-JF7L7FJFJFLJL7FJL7|L7L-7L7L7||7|F---7F-----7L-7|F--------J|F7FJ||L7F7||FL-
LJL-J7.L.FFJF---JL-JFL----JF-7L7|||L---7LJL-7|FJ|LJ||L|L7L7L-7||L7FJ|FJ|FJF77F7|L7FJL7L7FJFJFJ|L7FJF-7||F---7|F-J|L------7F7||LJJLJFLJLJ-77L
|F|J.|.|7FJFJ-F---7FF---7F7L7L-J|||F---JF7F7LJL7L-7||FJFJ7L7FJLJLLJFJ|-||L||FJLJFJL7FJFJL7L7L7|FJL7|FJ|LJF--JLJF7L7F7F7F7LJLJL--7F7F--7J-77J
||7-|LFFLL-JF-JF-7L-JF-7LJ||L--7LJ|L----JLJL--7|F7|LJL7L7F-JL-----7L7L7|L-J|L-7FJF-JL7|F7|FJFJ||F7LJL7L-7|F---7||7LJLJLJL7F7F---J||L7FJJ--J.
FL|FLF|7FLF7L--JFJF--JJL-7|F7F7L-7L-----------JLJ||F--JFJL--7F-7F-JLL7||F--JF7||LL-7FJLJLJL7L7||||F--JF7LJ|F--J|L7F7JF7F7LJLJF7F7|L7|L7|-77.
7-LJ-JJF7||L---7L-JF-----JLJ|||F-JF-------7F7F--7LJL--7L7F--JL7|L---7|||L--7|LJL--7|L7F-7F7L-JLJ||L---JL--JL--7|FJ|L-JLJL---7||||L7LJFJ77L77
F7-L-7.|L7L---7L7F-JF7F7F7F7LJLJF7|F------J|||F-JF7F-7|FJL-7F7||F-7FJ||L7F7|L-7F7FJ|FJL7LJL---7FJ|F7F7F7F----7LJL7L7F-------J||||7|F-JF7|FJ|
F7||L--L7L--7L|FJL--JLJLJLJL-7F7|LJL-7F7-F7|LJL-7||L7LJL-7.|||||L7|L7||FJ|LJF-J||L7||F-JF----7||FJ|LJ|||L---7L---JFJL-7F7F7F7|LJL-JL-7|L77L|
|L|FF..LL--7L-JL7F7.F-----7F-J|||F---J|L7|LJF7F7LJL7L7F-7L7LJ|||FJL7|||L7|F-JF7||FJLJL-7L7F-7|LJL7L-7||L----JF-7|FJF--J|||LJ||F--7F-7LJFJJ..
F-FJ|-|JLJJL---7LJL-JF7F-7|L--JLJL--7FJFJ|F-JLJL---JFLJLL7L-7||||F7LJ|L7||L7FJLJ||LF77FJFJL7LJF-7|7FJLJF-7F7FJFJFJFJF7L|||F-J||F7LJFJF-JJ-77
|.LL--J7F7F--77L-7F--JLJFJL----7F---J|FJFJL----------7-F7|F-JLJ|LJL-7|FJ||FJ|F--JL7|L7L-JF7L--JFJL-JF--JJLJLJFJLL7|FJL-JLJL77|LJL-7L-JF7|F77
|7.F|7-JJFL-7|F-7LJF-77FJF----7|L---7||FJF-7F7F--7F--JFJLJL-7F-JF-7FJ|L7||L-JL--7FJL7L77FJL-7F7L--7FJF-------J|F7|LJF-7F--7L-JF--7L---J|J-J|
J7FL--.|-F--J||FJF7|FJFJFJF--7||LF7FJ||L7L7|||L-7|L-7-|F7F--J|F7|FJL7L7|LJJJF7F-J|F7L7L7L--7|||FF7LJFJF7F------JLJF7|FJL-7L-7FJF7L----7|J--7
|7LLL7LJ-L--7LJL-JLJL7L7L7L-7|||FJLJFJL7|FJLJL7FJL-7L7|||L--7||LJ|F7L7|L-77-|LJF7||L7L7L---JLJL-JL-7L-JLJF7F7F--7FJ||L7F7L7FJL-JL----7LJF7--
.F-|LL.|F--7L7F7F7F-7L-JFJF7|LJLJF-7L7FJ||F7F7LJF77L7|LJL7F-JLJFFJ||FJL--J-FJF7|LJL7L-JF7F--7F--7F7L-----JLJ|L-7||.||LLJ|FJ|F7F-7F---J|L|-F7
||7FJ|-FL-7L7LJ||LJFJF-7|FJLJF-7FJ.L-JL-JLJLJ|F7|L-7LJF7-|L7FFLFJFJ|L-7JJJ7L7||L7JJL7F7|LJF7|||FJ|L7F7F7F-7JL7FJ|L7LJF7JLJJ||||L|L-7F-7LJ7JF
F7-|JLF-7FL7||FJ|F-JFJFJ|L-7FJFJ|F--7F--7F---J|LJF-JF7|L7L-JF7J|FJ-L7FJJL||LLJL-JJL|LJLJ|FJLJL7L7|FJ|||LJFJF7LJ-L7L7FJ|F7F7|||L7|F7LJFJ7|.FJ
FJ||.|L7|F7|L7L-J|F7L7L-JF7LJ7L-JL-7|L-7|L----JF7L-7|||FJ7F-J|FJ|J|FJ|J--7LFJ.|JL-FF7F7F7L7F7FJJLJL7|LJF-JFJ|LF7-L-JL7||LJ|||L7|||L-7|F--F-|
.FJ|FJ||LJLJFJF7.LJL-JF--JL--------JL--JL------JL-7LJ||L--JF7|L-J-FJFJ-7JLF|7F77J7FJLJ||L7LJLJF7-F7LJF7L-7L7L-JL7-F7FJLJF7|LJJLJ||F7LJF|.L7F
F--7J.FJF7F7L-JL77F7F7L--7F7F------7F-----------7FL-7LJF7F7|LJ-LJ.L-J|-7.FFJJ.L-.FL--7||FJLF-7||FJL--JL--JFJF7F7L7|||F--JLJF7F-7|LJL---7.LF-
J..|.L|FJLJL--7FJFJLJ||F7LJLJF-----J|F-------7F7L7F7L-7|||||J|..|.|L.7J|-J|7L7J.L|F7J|LJL--JFJ||L7F-------JFJLJL7LJ|||F-7LFJLJFJL7F----J7-FJ
F77F7.LJ.FF---JL7L-7FJFJ|F--7L--7F--JL---7F77LJL7LJL7FJ|LJLJ7L7FF-7FJ|.LJ-|-JL7.|FJL-JF--7F7L7|L7LJ-F7F-7F-JF7F7L--J|||FJFJF7FJF7LJF7JJJL7J7
F|-|.-|77FJF-7F7L--JL7|FJL-7|F7JLJF---7F7LJL---7L7F-JL7L----7-L|7.-7.-7L|||J||F7LL7F--JF7LJL7||FJF7FJLJFJL--J||L-7F-JLJL-JFJLJFJL--J||7||JF-
77LLJ-F-7L7|7LJL7F7F7LJL7JFJLJ|F7.L7F7LJL------J.LJF-7|F7F7FJJ.F-7L|FJJ.-7J.L-JFLFJ|F--J|F--JLJL-JLJF-7|.F7F7LJF7LJF7F7F7FJF--JF7F-7L7--J.F|
F7.F|FL7|-LJF7F7LJLJL--7L7L--7|||F7LJL7F------7F---JFJ||||LJ|7F7-F-|J|F7---7.L--JL-JL--7|L----------JFJL-JLJL--J|F-JLJLJLJ7|F--JLJ-L-JJ|LFLJ
|L7-F7FJL7F7|LJL-7F7F7F|FJF--JLJLJL---JL-7F7F7LJF7F7L7||LJF7F7JJFJ7L7--JJJF|J7L7FF-----J|F----7FF7F7FJF7F7F----7|L-------7FJL----77JL7F-7JJ.
L7L7||L7FJ||L-7F7LJLJL-JL7|F---7F------7J||||L--JLJL-JLJ7FJLJ|J.|-JJL7JF.FJ-.7JF-L-----7LJF7F7L-JLJLJFJLJLJF7F7|L7F7F----J|F-----JF7-L7JLLL|
LL7LJL-JL-J|F7LJL-------7|LJF7LLJF-----JFJ|LJF--7F7F7F7F7|F--J.F|7|FFJ|L7J|J7LLL7F-----JF-JLJ|F7F-7F7|F----JLJ|L7|||L-7F--JL------J|-F77L-.|
.LL7F-7F7F7LJL-----7JF7FJ|F-JL7F7L--7F7J|FJF-JF-J|||LJ||||L---7F7J7|JLF7J.L7|7-|L|F----7|.F7FJ|||-LJLJL------7|FJ|||F7LJF7F7F------J.FLL-|-|
|FFJ||||LJL7F---7F7L-JLJFJL--7|||F--J|L7||-|F-JF7|LJF-J||L7F--J|L7-JJ.F7--F77L-7JLJF---J|FJLJFJ||F-7F7F7JF7F7|LJFJ|LJ|F-J|||L7F7F---7J7.77.J
|-L7L7LJF--J|F--J|L----7|F7F7||||L-7-|FJ|L-JL-7|LJF-JF-J|FJL--7|FJ7|J-|L7F||7.LF---JF-7FJL7F7|FJ|L7LJLJL-JLJLJF7L-JF7||F-J|L7LJLJF--J--7LL|J
JLLL-JJ|L-7FJL---JF----JLJ|||||||F7L-JL-JF7F--J|F-JF7L-7||F---J|L7-J.FL7|FJ|J7JL--7FJFJ|F7LJLJL7|LL--7F--7F7F7||F7-||LJ|F7L7L7F-7L---7FF7-||
LFJJ.|F77FJ|F-----JF--7F-7LJLJLJLJL---7F7|LJF7J||F-J|LFJLJL-7F7|FJJL--FJLJFJLJFF7|LJ.L-J||F----J|F7F7LJF-J|LJLJLJL-JL-7LJL-J-||FJF---J7-7FL-
FJLF7F|L-JFJ|F-----JF7LJFJF-7F-7F7F--7|||L-7|L-JLJF7L-JF---7||LJL-77|FL-7FJF7|FJ|-F7F---J|L-----J|LJL--JF7|F----7F----JF-7F-7||L7L----7J|7FJ
L-JJF-JF--J|LJF7F7F-JL-7L7|FJ|7||LJF7||||F7LJF7F-7|L7F7L--7||L7F--JJFFFFJ|-L-LL7L7||L---7L-----7LL---7F-JLJL---7|L----7L7LJFJLJJL-7F-7|FFJ.7
FLJJL--JJF--7.||||L7F-7L-J|L7|FJ|F-JLJLJLJL7FJ|L7|L7LJ|F--JLJ||L--7F7JFJFJJ|LL-L7||L7F7|L-7F7F7L-----J|F--7F7F-JL-7F-7L-JF7L7FLF-7LJLLJJJ77F
|F--L.|F-L-7L-JLJ|FLJ|L---JFLJL-JL---7F7F7.LJJL-JL7L-7|L7F--7FJF--J||J|FJF--7J7FJ||FJ||F7.LJLJL---7F--J|F7LJLJLF7L|||L-7FJ|FJF7L7|F7L|F|LFJ|
|L77LFJL-LFJF7F-7|F--7F7FF----------7LJLJL-------7L--JL7LJF-JL7|-F7||FJL-JF-JLFL7||L7|||L7.F7F----J|LF7LJL7F---JL7LJF-7LJFLJFJL-JLJL-7F|-J.|
L-F7.J.|LLL7|||FJLJF7LJL-JF--7F7F--7|F-7F---7F---JJF7F7L--J-F7|L7|||||F7F7|.LF--J|L7||LJFJFJ|L-----JFJL---JL7F---JF7L7L-7F-7L-7F----7L77.LLJ
J|L||.-|.|.LJLJL--7|L-7F--JF-J|||F-JLJL|L--7LJF7F-7|||L-7F7|||L7LJ|||||LJLJF7L7F7L7|||F7L7L7|LF7F---JF---7F7||F7F7||FJF-J|FJF-JL---7L-JJ.L-|
FL-J||F-7.F------7|L7FJ|F--JF7|LJL----7L--7|F-J||FJ|LJF-J|L-JL7L-7||||L---7|L7LJL7|||LJL7L-JL-J|L----JFF7LJLJLJLJLJLJFJ-FJL7L7F----J|7L-7-7J
J|.L-LL-F7L---7F7LJFJ|FJ|F7FJLJF7F7F--JFF7LJL-7LJ|FJF7|F7L--7FJF7|||LJF7F-JL7L7FFJLJL--7L-----7|JF7F7F-JL------7F----J7FJF7|FJL7F---7-7|F7|J
F-JJ.||.LF7F--J||F7L7|L7||LJF--J||LJF7F7||F7F7|F-J|FJLJ||F7FJ|7|||LJF-JLJF7FJFJFJF7F---J-F----JL-JLJ|L-7F-----7||F---7FJFJ|||F-J|F--JJ7F|FJ.
JJ--L-F--J|L---J||L7|L7|LJF7L--7|L--JLJLJLJ||||L--J|F7FJ|||L7|FJ||F-JF-7FJ|L7L7L7|LJF-7F7L7F--7F---7||FJ|F---7|LJ|F--J|FJ-LJ|L--JL7F-7-F-7.|
F|J.L-L7F7L-----JL7LJFLJ.FJL-7FJL----------J|LJF7F7LJLJFJ|L7|||FJ||F-JFJL7|FJFJFJL7JL7|||LLJF7LJLF-JL7L-JL--7LJF7||F77|L7F7FJF--7FJ|FJFL7L77
---.FJJLJL7F-7F---JJF-7F7L7F7LJF-7F7F7F7F7F-JF-JLJ|F7F-J.L7|||||||||F-JF-J|L7|FJF-JF7|LJL-7FJL---JF7FJF-----JLFJLJLJL-JFJ|||FJF7||L|L7F7|FJ|
FL|--77LJJ||FJ|-F7F7L7LJ||LJL-7L7LJLJLJ||LJF7|FF77LJLJF7F7||||||FJLJL-7|F7|F||L7L-7|LJF7F7|L-7F---J|||L----7F7|F--7F7F7L-JLJL-J|LJFJFJ|LJL-7
|LL77||L|LLJL-JFJLJL-JF7|F7F--JFJF-----J|F-JLJFJL7-F7FJ||LJLJ||LJF-7F-JLJ||FJL-JF-JL-7|LJLJF7LJF7F-J|F77F-7LJLJL-7LJ|||F7F-----JF7|FJ7|F7F7|
|JF-L-J.LJFF---JF-----J|LJ|L---J-L------J|FF7.|F7|FJ||FJL---7LJF7||LJ-F7FJ|L---7|F7F7||F77FJ|F7||L-7LJL7L7|F7F7F-JF7LJ||||F-----JLJ|7FJ|LJLJ
F-7|L|FL.FFJF-7FJF--7F7L-7L-7|F7FF7F-7F-7L-JL7|||||FJ||F7|F7L7FJLJF--7||L7L7F-7|LJLJ||LJL7L7LJLJL7|L--7L-JLJLJ|L--JL-7|||LJF7F-----JFJFJJ7.J
J|LL.77..F|FJFJL7L-7LJL-7L-7|FJL-JLJ|LJFJF7F-J||LJ|L7|||L7||FJ|F77L-7LJL7L7|L7||F7F-JL7F-JFJF7F-7|F---JF-----7|F7F7F7||||F7|LJF----7L7|J-L7|
J7-JF||F7LLJJL--JF-JF7F7L--JLJF-------7|FJLJF7|L-7L7|||L7|||L7||L7F7|F--JF||FJ|||LJF--J|F7L7|||-|LJF7F7|F----JLJLJLJLJ||LJ|L77|F---JFJL77.--
LF.7-F---7|-|-F7FJF7|LJL7F-7F-JF7F----JLJF-7|||F7|FJLJL7||||-|||FJ|LJL7F7FJLJFJ|L7FL--7LJL7LJLJFJF7|LJLJL---7F7F7F7F7|LJF7L7L-JL7F7L|F-JJF|7
FFFJ||-|FJ.-F-JLJFJLJF7LLJ.||F-JLJF7F7-F7L7|||||LJL---7|||||FJLJ|L|F--J||L-7FJLL7L-7F-JF--JF--7L7|||FF7F7F--J|LJLJLJL7F7|L7L---7LJL-JL-7J-7J
|JL-|7JF|-F-L--7FJF--JL--7FJ|L----JLJL-JL-J||LJL7F-7F-J|||||L7F7L7|L7F7||F-J|F7FJF-JL-7L77FJF-J|LJLJFJLJLJF7FJF7F-7F-J|||FJF7F7L--7F-7FJJ.LJ
|.7-|LF7J.F.LF-J|7L-----7|L-JF------7F-----JL7F-J|FJL-7LJLJ|FJ|L-JL7LJLJ|L-7|||L7L-7F7L7L7|FJFF--7F7L-7F-7|||FJ||.LJF7||||FJLJL--7|L7|L7L-7|
F7LLFF|J.F||FL--JF-7F7F-J|F--JF----7||F---7F7|L--J||F7L7F-7LJFJF-7JL7F--JF-J||L7L7FJ|L7L7LJ|F7L-7|||F-J|FJ|LJL7LJF7FJLJLJLJF---7FJ|FJL7|.|7L
LJ7.7.|LF-7-F--7.L7||||F7|L---JF---JLJ|F--J|||F---JFJ|LLJFJF-J7|FJF7|||F7L-7||FJJ|L7L7|FJF-J|L7FJLJ|L--JL-JF7FJF7|||F---7F7L--7|L7|L77LJ7J|J
.7-FJF|JLF|JL7FJF7||||LJ||F---7L----7FJ|F7FJLJ|FF7-|FJF7FL7L7F7|L7|LJ|FJL7FJLJL-7L7L7||L7|F7L7|L--7|.F7.|F7|||F|||||L-7LLJ|F-7||FJL-J-|7|FJ7
7JFL7.L7|L-F-JL-JLJLJ|F7|LJF-7L-----JL7LJ|L--7L7||FJL7||F7L7LJ||FJL7FJL7FJL--7F-JJL7LJ|FJ||L7||F7FJL7|L7FJLJ|L-JLJLJF-JF-7|L7LJLJJLFL-L|J.F-
||FFF--JLFJL--------7LJLJF-JFJF7F7F7F7|F-JFF7|FJ||L7FJ|||||L7FJ||F7||F7|||F7|||F77|L7FJ|FJL7|||||L7FJL7|L--7|F7F7F-7L7FJFJL-JJF7F7F7J..--FJ7
|F--J.J-FLFJF-------JF7F7|F7L7|||LJ||||L7F-J|||FJ|FJL7||||F7|L7|||||||||L7|L7|LJL7F7||FJ|F7||||||FJL7FJ|F7FJLJ|||||L7LJFJ.F7F-JL7F7J-F7..-7L
|||J|.LF-J.FL--7F----JLJLJ|L-J|LJF7LJ||FJL7FJ||L7||LFJ|||LJ||FJ|||||||||JLJF|L-7FJ|||||J||LJLJ||||F-JL7LJ|L--7LJ|L-7|F7|F7|LJF-7LJ|J.|J7L-J7
LL--7...|F-JFF-J|F-7F-----JF-7|LFJL--J||F7|L7||FJ|L7L7|LJF7LJL7|||LJ||LJF---JF7|L7|LJ|L7|L---7||||L-7FJF-JF--JF7|F-J|||LJLJF-JFL--J..|LJL7LL
FL|-|--|JLF77L--J|FJL--7F7FJFJL7|F7F-7|LJLJ-|||L7|FJFJL--JL--7LJ|L7FJL7FJF7F7|LJ|||F-JFJ|F7F7||||L-7|L7|F7L---J||L-7||L7F--JJF---7|FF7.L7J.|
LF-FJJ-||L-JF7F7FJL----J|||LL7FJLJLJ||L7F---J||FJ|L7L7F7F-7F7|F-JFJL--JL-J|||L--7|||F7L7||||LJ|||F-J|FJLJ|F7F7FJ|F-JLJFJL----JF--JF-JL77|...
L--|L-.F7-|.|LJLJF7F--7FJ|L7JLJF7F7F-JFJL---7|||.L-JFJ||L7LJLJL7FJJF------J||F7FJLJ|||FJ||||F-J|||JFJL--7|||||L7|L---7|F7F7F-7L---JF7FJ-F--F
.L-|7L7|F-J-L---7|LJF-JL7L7|F--JLJLJF7L7F---J||L7JF-JFJL7L7F--7|L-7L7F---7FJLJ||F-7|||L7|||||F7||L7L7F7FJ||||L7|L7F-7|LJ||LJ-L7F---JLJ||||FJ
7-F--77FF-L-LF--JL-7L---JJLJL7F7F--7||FJ|F7F7|L7|FJF7L7J|FJL7FJ|F7|FJL7F-JL-7|||L7LJ||FJLJ|||||||FJJ||LJFJ|||F|L7|L7|L7FJL7F77|L77||JFJ---L7
FFLJ.LL|J7JFFL7F7F7|F---7F7F7LJ||F-J||L7||LJ||L|||FJ|FJFJL--J||LJLJL7FJL7F-7L7LJ-L--J|L--7|||||||L7FJL-7L-J|L7|FJL7||FJ|F7LJL7|FJ--7-|JLJ7-|
LJ7-7JFLL-7LFFJ||||||F-7LJLJL--J|L7FJ|FJ||F-JL7||||FJL7|F7F-7|F-7F--J|F-JL7|FJF------JF7FJLJLJLJ|FJ|F-7L--7L7|||F7||LJFJ||F7FJLJ-L-JJL--LJ7|
FF7JL-F||-7.|L7||||||L7L-----7F7L7||FJL7LJL-7FJLJ||L7FJLJ|L7|||FJL7F7|L-7FJLJFJF---7F-J|L-7|F---JL7|L7L7F7|FJ||LJ||L-7L7|LJ|L-7F7F7.L-7.|FF7
LLJ|L7.L7-F-7JLJ||LJL-JJF7F-7LJ|FJ|||F-JF7F-JL--7||FJL--7L7||LJL-7||||F-J|7F7L-JF7FJL-7L-7L7|F--7FJL-J7LJLJ|FJL7FJ|F7|FJ|F-JF7|||-L.FJF7J-L7
LJ-|-J7.LL|FJF7.LJF-7F7FJ|L7L--JL7||||F-J|L-7F-7|LJ|F7F7L7LJ|F7F7|||LJL-7L-JL7F-JLJF7FJ7FJFJLJF-JL--7F7F-7FJL7FJL7LJLJ|FJL7FJ|LJL7|L.FF7.FFJ
..FJ..L7LFJL-J|-F7|FJ||L7L-JF-7F-J||LJL-7|FFJL7|L-7||LJL7|-FJ||||||L7F7FJF7F-JL--7FJ|L-7L7L--7L7F7F-J||L7|L7FJ|F7L---7||F-JL7|F7FJ7.F-L|.F-.
F-JF-7FJ-L-7F7L-JLJ|FJL-JF-7|FJL-7LJF-7L|L-JF7|L7FJ|L-7-||FJFJ||LJL7|||L7||L-7F7FJL7|F7L7|F7FJLLJ||LFJL7|L7LJ7||L7F7FJLJL-7FJLJLJF|-F7LJFFJ|
.L77JF7JFLFJ|L7F--7|L7F--JLLJL7F-JFFJFJFJF-7||L7|L7|F7|FJ||FJFJ|LF7|LJL7|||F7|||L-7|LJ|FJLJ||JF--JL7|F-J|FJF-7LJF|||L7JF--JL77.L7LL-|JLFLL-F
F.|J|LLFJ-L-JJ||F-JL-J|7F-----JL--7L7|FJFJL|||FJ|FJ|||||FJ||FJFJFJLJF--J|||||LJ|F-JL-7LJF7JLJFJF7F7LJL--JL-JFJFF7||L7|FJF7F7L-7F7.|||F-J.FL|
L.F7FJF|J7J-||LJL7F7F7|FJF-7F7F7F-JFJLJFJLFJ|||LLJJ|||||L7LJL7L7L7F7L-7FJ||||F7||F-7FJF7||F77|FJ|||F-7F-7F-7L-7|LJL7||L7|LJL7FJ7LF7-|7L7---F
|-77.7LJLJ7.LJ.|LLJ|||||FJ.LJ||||F7L--7L-7|FJ|L---7|||||FJJF-JFJFJ|L7FJL7|LJ||||LJFJL-JLJLJ|FJ|FJ||L7LJFJL7L--JL-7FJ||FJL-7LLJJ-...LJ7.JF|F7
L-LJ-J-J.||F-.JJ|JLLJLJLJF7F-J||||L---JF7|||J|F7F-JLJLJ|L-7L7FJFJFJFJL-7|L-7|||L7|L-7F7F7F-J|FJ|FJL7L-7L-7L----7FJL7LJ|F--J-JJ.|FJJ.J-F.7L7J
L7F||.LFF|||-||FF7.F-----JLJF7|LJ|F7F7FJ|||L7LJ|L--7F-7L7FJFJ|-L-JFJF7FJ|F-J||L7L7F-J|LJ|L-7||7LJF7|F-J7FJF7F--JL7FJ|L|L-7L-|F-J77.FL7.-JFJJ
|.FL7.L-LJL-.L|FL-FL-7F-7F--J||7FJ|||||FJ|L7L-7|F--J|FJLLJ|L7|F---JFJ|||||F-JL7L7|L-7L-7L7FJLJF--JLJL--7|FJ|L--7-LJ-77L--J.L7J-FJ7-JL|--7-J|
F7-LJ-F|.|-J|J.|J|F--J|7||F7FJL7L7||||||FJFJF7||L---JL--77L7||L--7FJFJL7||L7F7L7||-FJF7L7|L7|LL7F-7F7F-J|L7L7F-JF|L--|LJ.J77L7FF-7F--JJ7||L-
L|LLJ-F|7F-FJ.|J--L7F7|FJLJ|L7FJFJ|LJ|||L7|FJ|||F--7F7F7|J|L||F--JL7L7FJLJFJ|L7|||FJFJ|FJ|FJ7J7LJ-LJ|L-7L7L7|L7-|7--|J7-77F77.-LFJ|.L7.|L77|
.7-L.FJL-JF|.|L|J.LLJ||L7F-JFJ|7L7L-7LJ|FJ|L7||||F7LJLJLJ-FJLJL7F7FJFJ|-|FJFJFJ|||L7L7LJ7|L7JL-.|7.|L7FJFL7||FJ|L-7FL-F7F-.7J|LL|7JJ7L||.L|7
||7|.|F7JF7-7JLJJ7LLLLJ-||JLL7|F-JF7||FJL7L7||||LJL7LF77|7|FF--J|||FL7L-7L-J-L7|LJFJFJ|LFJFJLF7-L7.-JLJ|LJLJLJJJFJ-LJ-|F7|-F7|F|LFJ.L7L-L.|L
F-JLLL.FFF-7|777-LF-7-LJLJJ.LLJL-7||L7L7FJFJ|||L7F7L-JL7.LJLL7F-J||7J|F7L7-||LLJF-JFJ|FLL-JJ.LJ|7L7F77LL..|F||JJ7LJJ|L-L7J7.FL-J-L.7L-7JJ7F|
|.J..LL7L|J-L||FJFL--.|.|-L-F7F--J||FJ-||-L7||L7LJL7F-7|FFFLFJ|7.LJLFJ|L-J-L-L7|L7FJLLF.|JLLF7-LL7JL-7J|7FLJ7JJ7|JL-J.L||J7-7|L|7L----J77FF|
L-J7-|LF-J-L-7J-F7F7JFJ-FFJ|F-JF7FJ||7LLJF-J|L7L7FL|L7LJ77FJL7|J-7|7L-JJ|.|L77L-.LJJ7.LLJ.FL|77||J.|FL7|F7.|JJ7|.FL7LF--JJL7|FJL-.L|-7L-7L|J
||LL.7|.7F7.7.|.|LJJFJ|--FJLL-7||L7||--LJL-7L7L7|J-|FJ7L.7.|FJ||7L-7.|JLF-7L7-JJ-||-FL7-J.7|.|FL|.FJLLJL-JFL-FFLL..|JLJLL-|-F|7|.|-LF.-.JFL.
F77LF|JF|-LJJF-7LF7.|-|-LJ7F|JLJ|FJLJJJ|7.FJFJ-||LFLJ|L.|..FL7|7J.||LJF7LLFJL||F77|F-J|F-J-7-|-7JF77JLJ-LFF.L7JFL7.FF7|L|L7|.J-L-77.LF7-7L-|
-JF7||7F7-7|.F7LJL7-F7|.F7F|J|LL|L7J|.FL--|FJ.|LJ.F-LF7F7---FJ|J|.F|JFLJ-7|JJL7-|L7JJF7J.|LJ.L|7FJ.|F7L|L||J.L-L7-L.F|7-L.L--J7L7L77J.L-JL7J
L-JL-|---.J-7|7|.F7-JF----FJL-7-|FJ|LFFF--LJ|F-|-7|J|LL||FJLL-J-FF-|JFL7L|JL7.L--JL|JF|L|-F.---|J|FJF|7L7L|FFF.LFF.F-7|||7JFF|-J7FLFJ7.F|FLJ
|-J.LLJFJ-JL|.J-7LJ-7.LFJ7L|-FJ-||.|||LJ|.L7|JLJL-F-F7LL|-7-LLL..|-J.L.|F|F--777LLF--||F|F7J7.|JL7-L7.-7L7LJ7|-FF|-7-7JFJ7---77|-7.L-FJFF7J|
77LL-J.-JJ-F--L-J-LF-F--7-.--|--LJ-FL-JJL7.7-JJ.FLJ-7-JLLL--7-|-|LLL7.--J.JJ-LF7-LLJ-L|J-LJ.LL7.LFJ.L|L-J--LL|7-7LJ-J|-7-J.|JL|JJ.7-L|JLJL.L
""".strip().splitlines()
input
# %%

start_coord=[(i,input[i].index("S")) for i in range(len(input)) if "S" in input[i]][0]
start_coord


# %%

def next_pos(current_symbol:str, current_coord : tuple, direction : str):
    next_coord = current_coord
    next_direction = current_direction

    if current_symbol == "|" and direction =='south' : 
        next_coord = (next_coord[0]+1,next_coord[1])
        next_direction = 'south'
    elif current_symbol == "|" and direction =='north' : 
        next_coord = (next_coord[0]-1,next_coord[1])
        next_direction = 'north'

    elif current_symbol == "-" and direction =='east': 
        next_coord = (next_coord[0],next_coord[1]+1)
        next_direction = 'east'
    elif current_symbol == "-" and direction =='west': 
        next_coord = (next_coord[0],next_coord[1]-1)
        next_direction = 'west'

    elif current_symbol == "L" and direction =='south': 
        next_coord = (next_coord[0],next_coord[1]+1)
        next_direction = 'east'
    elif current_symbol == "L" and direction =='west': 
        next_coord = (next_coord[0]-1,next_coord[1])
        next_direction = 'north'

    elif current_symbol == "J" and direction =='east': 
        next_coord = (next_coord[0]-1,next_coord[1])
        next_direction = 'north'
    elif current_symbol == "J" and direction =='south': 
        next_coord = (next_coord[0],next_coord[1]-1)
        next_direction = 'west'

    elif current_symbol == "7" and direction =='east': 
        next_coord = (next_coord[0]+1,next_coord[1])
        next_direction = 'south'
    elif current_symbol == "7" and direction =='north': 
        next_coord = (next_coord[0],next_coord[1]-1)
        next_direction = 'west'

    elif current_symbol == "F" and direction =='north': 
        next_coord = (next_coord[0],next_coord[1]+1)
        next_direction = 'east'
    elif current_symbol == "F" and direction =='west': 
        next_coord = (next_coord[0]+1,next_coord[1])
        next_direction = 'south'
    
    else : 
        print("Invalid next direction, not a loop")


    return next_coord, next_direction


# %%

next_pos("F", (1,2), 'north')
# %%

def find_adjacents(start_coord):
    return [
        [(start_coord[0]+1,start_coord[1]), 'south'],
        [(start_coord[0]-1,start_coord[1]), 'north'],
        [(start_coord[0],start_coord[1]+1), 'east'],
        [(start_coord[0],start_coord[1]-1), 'west'],
     ]

# %%
adjacents = find_adjacents(start_coord)

# %%
current_coord, current_direction = adjacents[0]

steps = 1
steps_list = []
while current_coord :
    current_symbol = input[current_coord[0]][current_coord[1]]
    if current_symbol!="S" :
        next_coord, next_direction = next_pos(current_symbol = current_symbol ,
                current_coord  = current_coord, direction  = current_direction)
        steps+=1
        next_symbol = input[next_coord[0]][next_coord[1]]
        steps_list.append([next_coord,steps,next_symbol])
        current_coord, current_direction = next_coord, next_direction
    else : 
        current_coord=False
# %%
len(steps_list)
# %%

def num_steps_function(current_c, current_d):
    steps = 1
    steps_list = []
    isloop  = False 
    while current_c :
        current_s = input[current_c[0]][current_c[1]]
        if current_s!="S" :
            print(current_s,current_c,current_d)
            next_c, next_d = next_pos(current_s,current_c,current_d)
            if not(next_c ==current_c and next_d == current_d):
                steps+=1
                next_s = input[next_c[0]][next_c[1]]
                steps_list.append([next_c,steps,next_s])
                current_c, current_d = next_c, next_d
            else : break
        else : 
            current_c=False
            isloop = True
    return steps_list, isloop

# %%
adjacent_0, isloop_0 = num_steps_function(*adjacents[0])
adjacent_1 , isloop_1 = num_steps_function(*adjacents[1])
adjacent_2,isloop_2 = num_steps_function(*adjacents[2])
adjacent_3 , isloop_3 = num_steps_function(*adjacents[3])
# %%

next_pos("L",(30,28),'north')
# %%

(len(adjacent_0)+1)/2, (len(adjacent_2)+1)/2
# %%

# %%

###################################

############ PART 2 ############
####################################
# symbols_to_consider = ['|','J','L','F','7']
# [i[0] for i in adjacent_0 if i[0][0]==0 and i[2] in symbols_to_consider]

(7,2) in [i[0] for i in adjacent_0 ]
#[i[2] for i in adjacent_0 if i[0][0]==0 and i[2] in symbols_to_consider]
#%%

symbols_inside = []
symbols_to_consider = ['|','J','L']
for row in range(len(input)):
    for col in range(len(input[row])):
        if (row, col ) not in [i[0] for i in adjacent_0 ]: 
            symbol = input[row][col]
            #print(f"For coord {(row, col)}")
            num_indices_left = len([i[0] for i in adjacent_0 
                            if (i[0][0]==row) and (i[2] in symbols_to_consider)
                            and (i[0][1]<col)
                            ])
            # print([i[0] for i in adjacent_0 
            #                 if (i[0][0]==row) and (i[2] in symbols_to_consider)
            #                 and (i[0][1]<col)
            #                 ])
            # print(f"num_indices_left = {num_indices_left}")
            num_indices_right = len([i[0] for i in adjacent_0 
                            if (i[0][0]==row) and (i[2] in symbols_to_consider)
                            and (i[0][1]>col)
                            ])
            # print([i[0] for i in adjacent_0 
            #                 if (i[0][0]==row) and (i[2] in symbols_to_consider)
            #                 and (i[0][1]>col)
            #                 ])
            # print(f"num_indices_right = {num_indices_right}")
            if (num_indices_left % 2 !=0 or num_indices_right % 2 !=0)and (num_indices_left!=0 and num_indices_right!=0 ) : 
                symbols_inside.append([symbol,(row, col)])
#len(symbols_inside)

# %%

len(symbols_inside)

# %%

symbols_inside

## 5, 78



# # Count wall intersections 

# num_rows, num_cols = len(input), [len(i) for i in input][0]
# print(num_rows, num_cols)

# coord_walls = [i[0] for i in adjacent_0]

# walls_row_list = []
# potential_Is_list = []
# for i in range(num_rows):
#     print(f"For row = {i}")
#     walls_row = sorted(list(filter(lambda x : x[0]==i , coord_walls)),key = lambda x : (x[1]))
#     print(walls_row)
#     walls_row_list.append(walls_row)

#     # Format = (row_number, start_range_wall_inclusive, end_range_wall_inclusive)
#     potential_Is  = [(i,walls_row[j-1][1]+1,walls_row[j][1]-1) for j in range(1,len(walls_row)) if walls_row[j][1]-walls_row[j-1][1]>1]
#     potential_Is_list.append(potential_Is)
#     print(potential_Is)





# # %%
# len(walls_row_list), len(potential_Is_list)
# # %%

# # Check if the potential_Is are both up and down of that row
# sum_I = 0
# for i in range(len(potential_Is_list)):
#     # if list is non-empty
#     if potential_Is_list[i] : 
#         walls_row_list_to_check_top = [k2 for k1, k2 in walls_row_list[i-1]]
#         walls_row_list_to_check_bottom = [k2 for k1, k2 in walls_row_list[i+1]]
#         print(f"Checking row = {i}")
#         print(f"walls_row_list_to_check_top = {walls_row_list_to_check_top}")
#         print(f"walls_row_list_to_check_bottom = {walls_row_list_to_check_bottom}")
#         for r_num, start_range_col, end_range_col in potential_Is_list[i] :
#             # range is present in both top and bottom
#             if ((sum([k in walls_row_list_to_check_top for k in range(start_range_col,end_range_col+1) ]) == len(range(start_range_col,end_range_col+1))) and 
#                 (sum([k in walls_row_list_to_check_bottom for k in range(start_range_col,end_range_col+1) ]) == len(range(start_range_col,end_range_col+1)))
#                 ):
#                 sum_I+=len(range(start_range_col,end_range_col+1))

#         #     break 

#         # break

# sum_I



# # %%
# # Check if the potential_Is are both up and down of that row
# sum_I = 0
# for i in range(len(potential_Is_list)):
#     # if list is non-empty
#     if potential_Is_list[i] : 
#         print(potential_Is_list[i])
#         for r_num, start_range_col, end_range_col in potential_Is_list[i] :
#             # range is present in both top and bottom
#             print(r_num, start_range_col, end_range_col)
#             sum_I+=len(range(start_range_col,end_range_col+1))
#             print(sum_I)

#         #     break 

#         # break

# sum_I

# # %%

# %%
