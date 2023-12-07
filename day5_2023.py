# %%

# seed_to_soil_map = """
# 3788621315 24578909 268976974
# 3633843608 2672619957 154777707
# 1562003446 2827397664 767899879
# 2618130896 293555883 1015712712
# 178572254 3595297543 462300746
# 640873000 1553961386 921130446
# 2373438105 1435027522 118933864
# 2492371969 1309268595 125758927
# 2329903325 2629085177 43534780
# 24578909 2475091832 153993345
# """

input = """
seeds: 929142010 467769747 2497466808 210166838 3768123711 33216796 1609270159 86969850 199555506 378609832 1840685500 314009711 1740069852 36868255 2161129344 170490105 2869967743 265455365 3984276455 31190888

seed-to-soil map:
3788621315 24578909 268976974
3633843608 2672619957 154777707
1562003446 2827397664 767899879
2618130896 293555883 1015712712
178572254 3595297543 462300746
640873000 1553961386 921130446
2373438105 1435027522 118933864
2492371969 1309268595 125758927
2329903325 2629085177 43534780
24578909 2475091832 153993345

soil-to-fertilizer map:
3438795585 3489901885 246180709
2207634271 2882741084 20404178
2921657379 3093830975 5578539
3684976294 494116589 47356386
3924272359 3740035076 65483093
501906244 2178419272 30310459
1234683323 1988217660 166809869
1901474422 3380297447 5929907
1561485292 902794130 43191607
3740035076 4064176085 35875061
1756130945 2337296126 107889556
1631134020 2212299201 124996925
3775910137 4100051146 148362222
1907404329 355795024 25976339
98608320 1132323727 78740039
177348359 323563608 17306027
3181146272 2546033985 176714999
1135867625 395300891 98815698
1604676899 381771363 13529528
1062398411 3348792067 31505380
1933380668 1211063766 135031541
4152704827 4248413368 14047124
2231607919 3386227354 49301269
2068412209 1349845221 139222062
1618206427 0 12927593
4166751951 3935960740 128215345
4055852131 3871614848 64345892
1093903791 340869635 14925389
2280909188 93861907 229701701
252523691 3099409514 249382553
194654386 640081295 34477562
2228038449 2208729731 3569470
2927235918 674558857 8851379
3989755452 3805518169 66096679
3732332680 1346095307 3749914
229131948 2155027529 23391743
1108829180 945985737 27038445
2510610889 683410236 219383894
2729994783 973024182 159299545
2936087297 2903145262 190685713
2889294328 1489067283 32363051
4120198023 4262460492 32506804
633065006 1558884255 429333405
3126773010 3435528623 54373262
0 541472975 98608320
3357861271 12927593 80934314
532216703 2445185682 100848303
1401493192 2722748984 159992100
1864020501 1521430334 37453921

fertilizer-to-water map:
1947541026 454827174 151424508
2368626375 2974348911 49282632
1180361458 1899400011 39609082
680762316 1808139816 91260195
3146089823 3660401583 124406340
1750346896 411180537 43646637
812988815 228261758 177656250
1318675555 1023120195 274976204
1593651759 866425058 156695137
3971733879 2669799085 75517075
3655228757 4176552157 118415139
3441507492 3915100392 170047342
3888713098 2412300298 83020781
552417940 99917382 128344376
1799256062 1298096399 110644443
0 825619231 40805827
123867918 1939009093 176811732
3835793763 4085147734 52919335
300679650 1712674949 32370741
772022511 1598457235 40966304
1219970540 1639423539 73251410
3297826708 3784807923 40826594
1793993533 405918008 5262529
3056623948 3825634517 89465875
3773643896 3023631543 62149867
1909900505 1770499295 37640521
40805827 16855291 83062091
2417909007 2745316160 229032751
3611554834 2368626375 43673923
2646941758 4138067069 38485088
4047250954 2598175269 71623816
3338653302 2495321079 102854190
2685426846 3279231811 71633749
4118874770 3085781410 165769241
3028942788 3251550651 27681160
333050391 606251682 219367549
2757060595 3388519390 271882193
1293221950 1745045690 25453605
3270496163 3350865560 27330545
4284644011 3378196105 10323285
990645065 1408740842 189716393
2098965534 0 16855291

water-to-light map:
1069022530 222696536 26137468
509774651 1001927432 264687540
2799496570 4178737505 91960917
2622746937 2920297784 87218886
998047684 72317843 70974846
20975330 248834004 16650836
1516625244 2418736444 445891562
867141089 265484840 130906595
1452450963 1912658188 64174281
2891457487 2382365765 36370679
837778702 42955456 29362387
3824593525 1874523410 38134778
87390794 857485915 142625628
3874640725 2075355481 18387003
774462191 529657635 63316511
3607044420 4131300557 47436948
2288390345 3657176164 11501412
3042932184 1976832469 64291113
2947540744 4035909117 95391440
87126518 42691180 264276
1425451487 3765808292 26999476
3893027728 3579750125 77426039
2203098143 3680516090 85292202
3992272144 3274151418 290856638
2927828166 4033389105 2520012
278763375 464023676 18702895
3114215141 1527053163 335557825
3654481368 3014508514 170112157
2930348178 3565008056 14742069
230016422 482726571 46931064
3970453767 4270698422 21818377
4283128782 3668677576 11838514
1223923792 0 42691180
3505442744 1425451487 101601676
2709965823 3184620671 89530747
1174563845 737650286 49359947
3862728303 1862610988 11912422
37626166 787010233 49500352
3449772966 2864628006 55669778
297466270 592974146 144676140
2334123656 2093742484 288623281
2945090247 4292516799 2450497
1095159998 143292689 79403847
3107223297 3007516670 6991844
0 836510585 20975330
2299891757 2041123582 34231899
276947486 1000111543 1815889
442142410 396391435 67632241
1962516806 3792807768 240581337

light-to-temperature map:
3884798542 3179257010 5536030
2221366309 1722332134 176062455
550850442 2239976316 812984276
1811481549 3100760963 78496047
2640090257 457193060 313876206
2495814208 2197536573 42439743
3995825312 1898394589 299141984
3754849534 3407613625 129949008
3890334572 3302122885 105490740
1889977596 771069266 255516805
3300733900 3052960592 47800371
3497312635 4294682795 284501
3348534271 3830987352 148778364
3181367714 3537562633 118078810
2397428764 3655641443 98385444
2563129792 3754026887 11234150
3497597136 3279737798 22385087
2538253951 1249809462 24875841
2953966463 4067281544 227401251
2145494401 3979765716 75871908
1363834718 1274685303 447646831
457193060 3184793040 93657382
3519982223 4055637624 11643920
2574363942 3765261037 65726315
3299446524 3278450422 1287376
3531626143 1026586071 223223391

temperature-to-humidity map:
1042511941 613297634 21380371
1338560988 2467432579 195807105
1689790100 2663239684 5147838
1534368093 1255646654 123554085
1657922178 472280060 31867922
1063892312 634678005 22101508
3020373353 2743804882 227587056
3354622010 3207836814 51442173
279315000 1414949840 172148078
2333443661 0 36016786
2656069043 859373847 9250148
81520987 1873230878 37317266
2452902712 868623995 174257482
2665319191 1042881477 3068331
1085993820 504147982 109149652
1875725935 36016786 328594859
3247960409 4062312657 86516416
2743804882 3833392893 10707972
2204320794 2254867447 129122867
1302811887 1379200739 35749101
3930773544 4267797728 7024383
4056766582 3259278987 238200714
1195143472 364611645 107668415
0 656779513 81520987
2369460447 2383990314 83442265
3334476825 4274822111 20145185
451463078 1910548144 344319303
811683287 1642402224 230828654
2754512854 3160188107 47648707
2802161561 3844100865 218211792
3741977375 2971391938 188796169
2627160194 1226737805 28908849
3406064183 3497479701 245403322
795782381 843472941 15900906
174142559 738300500 105172441
1694937938 1045949808 180787997
3651467505 3742883023 90509870
3937797927 4148829073 118968655
118838253 1587097918 55304306

humidity-to-location map:
561172837 465568195 974822499
3386805071 4164489434 100929125
1899981360 1440390694 188334950
459590666 0 101582171
0 1735512469 459590666
3517282933 3386805071 777684363
2088316310 1628725644 106786825
3487734196 4265418559 29548737
1535995336 101582171 363986024

salt:
""".strip()

# %%
import re
seeds = re.finditer(r'seeds: (\d+|\n).*',input)
seeds_list = [i.group().replace("seeds:","").strip().split() for i in seeds ][0]
seeds_list_int=list(map(int,seeds_list))

# %%

def create_mapping_list(pattern, input,replace_string, splitter = "\n"):
    seeds_to_soil_mapping = re.finditer(pattern,input)
    seeds_to_soil_mapping_list = [
        list(map(lambda x : x.split() ,i.group().replace(replace_string,"").strip().split(splitter)) )
    for i in seeds_to_soil_mapping
    ][0]

    print(seeds_to_soil_mapping_list)
    seeds_to_soil_mapping_list_int = list(map(lambda x : list(map(int, x)), seeds_to_soil_mapping_list))
    print(seeds_to_soil_mapping_list_int)
    return seeds_to_soil_mapping_list_int


# %%

seeds_to_soil_mapping_list_int = create_mapping_list(pattern = r'seed-to-soil map:\s+(\d+?\s+)+', 
                                                    input = input,
                                                    replace_string = "seed-to-soil map:", 
                                                    splitter = "\n"
                                                    )

soil_to_fertilizer_mapping_list_int = create_mapping_list(pattern = r'soil-to-fertilizer map:\s+(\d+?\s+)+', 
                                                    input = input,
                                                    replace_string = "soil-to-fertilizer map:", 
                                                    splitter = "\n"
                                                    )

fertilizer_to_water_mapping_list_int = create_mapping_list(pattern =r'fertilizer-to-water map:\s+(\d+?\s+)+', 
                                                    input = input,
                                                    replace_string = "fertilizer-to-water map:", 
                                                    splitter = "\n"
                                                    )

water_to_light_mapping_list_int = create_mapping_list(pattern =r'water-to-light map:\s+(\d+?\s+)+', 
                                                    input = input,
                                                    replace_string = "water-to-light map:", 
                                                    splitter = "\n"
                                                    )

light_to_temperature_mapping_list_int = create_mapping_list(pattern =r'light-to-temperature map:\s+(\d+?\s+)+', 
                                                    input = input,
                                                    replace_string = "light-to-temperature map:", 
                                                    splitter = "\n"
                                                    )

temperature_to_humidity_mapping_list_int = create_mapping_list(pattern =r'temperature-to-humidity map:\s+(\d+?\s+)+', 
                                                    input = input,
                                                    replace_string = "temperature-to-humidity map:", 
                                                    splitter = "\n"
                                                    )

humidity_to_location_mapping_list_int = create_mapping_list(pattern =r'humidity-to-location map:\s+(\d+?\s+)+', 
                                                    input = input,
                                                    replace_string = "humidity-to-location map:", 
                                                    splitter = "\n"
                                                    )
# %%

print(seeds_to_soil_mapping_list_int)
print(soil_to_fertilizer_mapping_list_int)
print(fertilizer_to_water_mapping_list_int)
print(water_to_light_mapping_list_int)
print(light_to_temperature_mapping_list_int)
print(temperature_to_humidity_mapping_list_int)
print(humidity_to_location_mapping_list_int)

# %%

print(len(seeds_to_soil_mapping_list_int))
print(len(soil_to_fertilizer_mapping_list_int))
print(len(fertilizer_to_water_mapping_list_int))
print(len(water_to_light_mapping_list_int))
print(len(light_to_temperature_mapping_list_int))
print(len(temperature_to_humidity_mapping_list_int))
print(len(humidity_to_location_mapping_list_int))

# %%

####### Map seeds_to_soil_mapping_list_int ############

seeds_to_soil_mapping_list_int


# %%

def create_mapping_dict(dest_start_range, source_start_range, range_len):
    lst_src,lst_dest = [],[]
    for i,j in zip(range(source_start_range,source_start_range + range_len),range(dest_start_range,dest_start_range + range_len)):
        lst_src.append(i)
        lst_dest.append(j)
    print(lst_src)
    print(lst_dest)
    dictionary = dict(zip(lst_src,lst_dest))
    return dictionary

# %%
# 99 -> 51 
# 99-98 = 1
# 50+1 = 51
create_mapping_dict(50 ,98, 2)
# %%


# %%
source_no = 929142010

def find_dest_no(source_to_dest_mapping_list_int, source_no ):
    dest_no = None
    for i in source_to_dest_mapping_list_int : 
        #print(i)
        dest_start_range,source_start_range , range_len  = i[0],i[1],i[2]
        #print(source_no in range(source_start_range,source_start_range + range_len))
        if source_no in range(source_start_range,source_start_range + range_len) : 
            diff_source = source_no-source_start_range
            dest_no = diff_source + dest_start_range
            #print(f"dest_no is {dest_no}")
            break
    return dest_no if dest_no else source_no


# %%

def find_location_no(seed_no):
    soil_no = find_dest_no(source_to_dest_mapping_list_int = seeds_to_soil_mapping_list_int,source_no = seed_no  )
    fert_no = find_dest_no(source_to_dest_mapping_list_int = soil_to_fertilizer_mapping_list_int,source_no = soil_no  )
    water_no = find_dest_no(source_to_dest_mapping_list_int = fertilizer_to_water_mapping_list_int,source_no = fert_no  )
    light_no = find_dest_no(source_to_dest_mapping_list_int = water_to_light_mapping_list_int,source_no = water_no  )
    temp_no = find_dest_no(source_to_dest_mapping_list_int = light_to_temperature_mapping_list_int,source_no = light_no  )
    humidity_no = find_dest_no(source_to_dest_mapping_list_int = temperature_to_humidity_mapping_list_int,source_no = temp_no  )
    location_no = find_dest_no(source_to_dest_mapping_list_int = humidity_to_location_mapping_list_int,source_no = humidity_no  )
    #print(soil_no,fert_no,water_no,light_no,temp_no,humidity_no,location_no)
    return location_no

# %%

find_location_no(929142010)

# %%
lst_loc = []
for i in seeds_list_int : 
    _loc=find_location_no(i)

    print(f"seed = {i}, loc = {_loc}")
    lst_loc.append(_loc)
# %%
min(lst_loc)

# %%

########################### PART 2 ###########################

# %%

start_range_seeds, range_len_seeds = seeds_list_int[::2], seeds_list_int[1::2]
print(start_range_seeds)
print(range_len_seeds)
print(seeds_list_int)
# %%

def create_seeds(start_range, range_len):
    return [i for i in range(start_range,start_range+range_len)]
# %%

create_seeds(79, 14)
# %%

def create_all_seeds(start_range_seeds, range_len_seeds):
    all_seeds = []
    for start_range, range_len in zip(start_range_seeds, range_len_seeds):
        print(len(create_seeds(start_range, range_len)))
        all_seeds.extend(create_seeds(start_range, range_len))
    return all_seeds

# %%
create_all_seeds(start_range_seeds, range_len_seeds)

# %%

def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

#%%

def binary_search(low, high):
    # Check base case
    lowest_loc = find_location_no(low) 
    
    if high >= low:
 
        mid = (high + low) // 2
        print(mid)
 
        # If middle ele is the lowest, return lowest (x)
        if find_location_no(mid) == lowest_loc:
            print(f"match found, mid = {mid}, lowest_loc = {lowest_loc}")
            return lowest_loc
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif find_location_no(mid) > lowest_loc:
            return binary_search(low, mid - 1)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(mid + 1, high)
 

#%%

binary_search(low =929142010 , high = 929142010+467769747-1)

# %%

_low =float('inf') 
temp = 0
for start_range, range_len in zip(start_range_seeds, range_len_seeds):
    temp=binary_search(low =start_range , high = start_range+range_len)
    if temp<_low:
        _low = temp

_low   

# %%
# def find_lowest_loc(start_range, range_len):
#     lowest_loc = -1
#     high = start_range + range_len-1
#     low = start_range
#     mid = (high + low) // 2

#     if find_location_no(mid) < find_location_no(low):
#         return mid
 
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
 
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)


#     for i in range(start_range,start_range+range_len):
#         if find_location_no(i)< lowest_loc : 
#             lowest_loc = find_location_no(i)

#     return lowest_loc


# %%
find_lowest_loc(929142010, 467769747)
# %%
_lst = []
for i in start_range_seeds:
    _lst.append(find_location_no(i))
# %%
_lst
# %%

min(_lst)
# %%
find_location_no(929142010),find_location_no(929142010 + 467769747-2 ),find_location_no(929142010 + 467769747-1 )\
    ,find_location_no(929142010 + (467769747//2) ),find_location_no(929142010 + (467769747//2)-10 )

# %%

# 56938496 -> 929142010 + (467769747//2)-100000
# 46938496 -> 929142010 + (467769747//2)-100000- (10000 + 10000000)
for i in range(100 ):
    print(find_location_no(929142010 + (467769747//2)-100000- (10000 + 10000000-i)))

46938495
# %%
