rank = input("What rank: \n1.Pubs\n2.Bronze\n3.Silver\n4.Gold\n5.Platinum\n6.Diamond\n7.Master")

map = input("\nwhat map: \n1.World's Edge\n2.Olympus")
if (map == "1"):
    pass
   # f = open("worldsEdgeDataFile.ods", "a")
if (map == "2"):
    pass
  #  f = open("olympusDataFile.ods", "a")

legend = input("\nyour legend: \n1.Bloodhound\n2.Gibraltar\n3.Lifeline\n4.Pathfinder\n5.Wraith\n6.Bangalore\n7.Caustic\n8.Mirage\n9.Octane\n10.Wattson\n11.Cypto\n12.Revenant\n13.Loba\n14.Rampart\n15.Horizon\n16.Fuse\n17.Valkyrie\n")
t1Legend = input("\nt1 legend: \n1.Bloodhound\n2.Gibraltar\n3.Lifeline\n4.Pathfinder\n5.Wraith\n6.Bangalore\n7.Caustic\n8.Mirage\n9.Octane\n10.Wattson\n11.Cypto\n12.Revenant\n13.Loba\n14.Rampart\n15.Horizon\n16.Fuse\n17.Valkyrie\n")
t2Legend = input("\nt1 legend: \n1.Bloodhound\n2.Gibraltar\n3.Lifeline\n4.Pathfinder\n5.Wraith\n6.Bangalore\n7.Caustic\n8.Mirage\n9.Octane\n10.Wattson\n11.Cypto\n12.Revenant\n13.Loba\n14.Rampart\n15.Horizon\n16.Fuse\n17.Valkyrie\n")

t1Level = input("\nTeammate 1 level: ")
t2Level = input("\nTeammate 2 level: ")

landLoc = input("\nland loc: ")
kills1 = input("\nKills: ")
secondLoc = input("\nSecond loc: ")
kills2 = input("\nKills: ")
thirdLoc = input("\nThird loc: ")
kills3 = input("\nKills: ")
fourthLoc = input("\nFourth loc: ")
kills4 = input("\nKills: ")
fifthLoc = input("\nFifth loc: ")
kills5 = input("\nKills: ")
    
dmg = input("\nDamage: ")
t1dmg = input("\nTeammate 1 damage: ")
t2dmg = input("\nTeammate 2 damage: ")
    
t1Kills = input("\nTeammate 1 kills: ")
t2Kills = input("\nTeammmate 2 kills: ")

weapon1 = input("\nWeapon 1 (primary): ")
weapon2 = input("\nWeapon 2 (secondary): ")
weapon3 = input("\nWeapon 3 (temporary): ")
weapon4 = input("\nWeapon 4 (temporary): ")
t1weapon1 = input("\nTeammate 1 Weapon 1 (primary): ")
t1weapon2 = input("\nTeammate 1 Weapon 2 (secondary): ")
t2weapon1 = input("\nTeammate 2 Weapon 1 (primary): ")
t2weapon2 = input("\nTeammate 2 Weapon 2 (secondary): ")

hasMic = input("\nHow many players used their microphones: ")
notes = input("\nAny special notes: ")

f = open("cock.txt", "a")
f.write("rank: " + rank + "\nmap: " + map + "\nlegend: " + legend  + "\nt1Legend: " +t1Legend  + "\nt2Legend: " + t2Legend + "\nt1Level: " + t1Level + "\nt2Level: " + t2Level + "\nlandLoc: " + landLoc + "\nkills1: " + kills1 + "\nsecondLoc: " + secondLoc + "\nkills2: " + kills2 + "\nthirdLoc: " + thirdLoc + "\nkills3: " + kills3 + "\nfourthLoc: " + fourthLoc + "\nkills4: " + kills4 + "\nfifthLoc: " + fifthLoc + "\nkills5: " + kills5 + "\ndmg: " + dmg + "\nt1dmg: " + t1dmg + "\nt2dmg: " + t2dmg + "\nt1kills: " + t1Kills + "\nt2kills: " + t2Kills + "\nweapon 1: " + weapon1 + "\nweapon 2: " + weapon2 + "\nweapon 3: " + weapon3 + "\nweapon 4: " + weapon4 + "\nt1weapon1: " + t1weapon1 + "\nt1weapon2: " + t1weapon2 + "\nt2weapon1: " + t2weapon1 + "\nt2weapon2: " + t2weapon2 + "\nhasMic: " + hasMic + "\nnotes: " + notes)
f.close()