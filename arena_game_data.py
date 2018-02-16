# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:46:23 2017

@author: arjunb
"""

import sys, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return True
    return False

def days_in_yr(year):
    if is_leap_year(year):
        return 366
    return 365

def get_game_distances(doy1, doy2, year):
    dist = np.zeros(len(doy1))
    most_recent_game = 0
    for i in range(len(doy1)):
        if doy2[0] > doy1[i]:
            dist[i] = np.random.randint(1, 21)
            continue
        
        for j in range(most_recent_game, len(doy2)):
            if doy2[j] > doy1[i]:
                dist[i] = doy1[i] - doy2[most_recent_game]
                break
            
            if j == len(doy2)-1 and doy2[j] < doy1[i]:
                dist[i] = doy1[i] - doy2[j]
                
            most_recent_game = j
    
    return dist

def convert_doy_b4_aft(doy_data, year):
    before_newYr = doy_data[:np.argmin(doy_data)]
    after_newYr = doy_data[np.argmin(doy_data):]
    fullY = days_in_yr(year-1)
    return np.append(before_newYr - fullY, after_newYr)

def results_daysAgo_avg(results_data):
    results_dict = {}
    for result, daysAgo in results_data:
        if result not in results_dict:
            results_dict[result] = []
        results_dict[result].append(daysAgo)
    
    for result in results_dict:
        sum = 0
        for daysAgo in results_dict[result]:
            sum += daysAgo
        results_dict[result] = sum / len(results_dict[result])
        
    return results_dict



team_pairs = (("76ers", "flyers"), ("nuggets", "avalanche"), ("bulls", "blackhawks"), 
              ("celtics", "bruins"), ("wizards", "capitals"), ("clippers", "kings"), 
              ("lakers", "kings"), ("knicks", "rangers"), ("raptors", "mapleleafs"), 
              ("mavericks", "stars"))

years = [2014, 2015, 2016, 2017]

def main():
    tic = time.time()
    
    for bkb_tm, hky_tm in team_pairs:
        bkb_data_doy_T = np.int64([])
        hky_data_doy_T = np.int64([])
        
        bkb_data_performance_T = np.int64([])
        hky_data_performance_T = np.int64([])  
        bkb_wins_T = 0
        bkb_losses_T = 0
        hky_wins_T = 0
        hky_ties_T = 0
        hky_losses_T = 0
        
        bkb_pointsFor_T = np.int64([])
        bkb_pointsAgainst_T = np.int64([])
        bkb_points_T = np.int64([])
        hky_goalsFor_T = np.int64([])
        hky_goalsAgainst_T = np.int64([])
        hky_goals_T = np.int64([])
        
        bkb_from_hky_dist_T = np.int64([])
        hky_from_bkb_dist_T = np.int64([])
            
        for year in years:
            bkb_data = pd.read_csv(sys.argv[1] + "/" + bkb_tm + str(year) + "home.csv")
            hky_data = pd.read_csv(sys.argv[1] + "/" + hky_tm + str(year) + "home.csv")
            
            bkb_data_doy = bkb_data["DOY"].values
            hky_data_doy = hky_data["DOY"].values
            bkb_data_doy = convert_doy_b4_aft(bkb_data_doy, year)
            hky_data_doy = convert_doy_b4_aft(hky_data_doy, year)
            bkb_data_doy_T = np.append(bkb_data_doy_T, bkb_data_doy)
            hky_data_doy_T = np.append(hky_data_doy_T, hky_data_doy)
            
            bkb_data_performance = np.int64(bkb_data["Result"].values)
            hky_data_performance = np.int64(hky_data["Result"].values)
            bkb_data_performance_T = np.append(bkb_data_performance_T, bkb_data_performance)
            hky_data_performance_T = np.append(hky_data_performance_T, hky_data_performance)
            bkb_wins = np.count_nonzero(bkb_data_performance)
            bkb_losses = len(bkb_data_performance) - bkb_wins
            hky_wins = np.count_nonzero(hky_data_performance == 2)
            hky_ties = np.count_nonzero(hky_data_performance == 1)
            hky_losses = len(hky_data_performance) - hky_wins - hky_ties
            bkb_wins_T += bkb_wins
            bkb_losses_T += bkb_losses
            hky_wins_T += hky_wins
            hky_ties_T += hky_ties
            hky_losses_T += hky_losses
            
            bkb_pointsFor = np.int64(bkb_data["For"].values)
            bkb_pointsAgainst = np.int64(bkb_data["Against"].values)
            bkb_points = (bkb_pointsFor + bkb_pointsAgainst) / 2
            hky_goalsFor = np.int64(hky_data["For"].values)
            hky_goalsAgainst = np.int64(hky_data["Against"].values)
            hky_goals = (hky_goalsFor + hky_goalsAgainst) / 2
            bkb_pointsFor_T = np.append(bkb_pointsFor_T, bkb_pointsFor)
            bkb_pointsAgainst_T = np.append(bkb_pointsAgainst_T, bkb_pointsAgainst)
            bkb_points_T = np.append(bkb_points_T, bkb_points)
            hky_goalsFor_T = np.append(hky_goalsFor_T, hky_goalsFor)
            hky_goalsAgainst_T = np.append(hky_goalsAgainst_T, hky_goalsAgainst)
            hky_goals_T = np.append(hky_goals_T, hky_goals)
            
            bkb_from_hky_dist = get_game_distances(bkb_data_doy, hky_data_doy, year)
            bkb_from_hky_dist = np.int64(bkb_from_hky_dist)
            bkb_from_hky_dist_T = np.append(bkb_from_hky_dist_T, bkb_from_hky_dist)
            
            
            """
            To get single-season plots, comment in
            
            plt.scatter(*zip(*list(zip(bkb_from_hky_dist, bkb_data_performance))))
            plt.title("Performance of  " + str(year) + " " + bkb_tm + " by days ago " + hky_tm + " played")
            plt.xlabel("Days ago " + hky_tm + " played")
            plt.ylabel("Game Result")
            plt.show()
            
            
            plt.figure()
            fit_bkb_for = np.polyfit(bkb_from_hky_dist, bkb_pointsFor, deg=1)
            plt.plot(bkb_from_hky_dist, fit_bkb_for[0] * bkb_from_hky_dist + fit_bkb_for[1], color="blue")
            plt.scatter(*zip(*list(zip(bkb_from_hky_dist, bkb_pointsFor))), label="Points For", color="blue")
            
            fit_bkb_against = np.polyfit(bkb_from_hky_dist, bkb_pointsAgainst, deg=1)
            plt.plot(bkb_from_hky_dist, fit_bkb_against[0] * bkb_from_hky_dist + fit_bkb_against[1], color="red")
            plt.scatter(*zip(*list(zip(bkb_from_hky_dist, bkb_pointsAgainst))), label="Points Against", color="red")
            
            fit_bkb = np.polyfit(bkb_from_hky_dist, bkb_points, deg=1)
            plt.plot(bkb_from_hky_dist, fit_bkb[0] * bkb_from_hky_dist + fit_bkb[1], label="Total Points", color="black")
            
            plt.title("Points scored in " + str(year) + " " + bkb_tm + " games by days ago " + hky_tm + " played")
            plt.xlabel("Days ago " + hky_tm + " played")
            plt.ylabel("Points")
            plt.legend(loc="upper right")
            #plt.show()
            
            #print("For: y = " + str(fit_bkb_for[0]) + "x + " + str(fit_bkb_for[1]))
            #print("Against: y = " + str(fit_bkb_against[0]) + "x + " + str(fit_bkb_against[1]))
            #print("Total: y = " + str(fit_bkb[0]) + "x + " + str(fit_bkb[1]))
            
            end of single-season basketball plots
            """

            
            hky_from_bkb_dist = get_game_distances(hky_data_doy, bkb_data_doy, year)
            hky_from_bkb_dist = np.int64(hky_from_bkb_dist)
            hky_from_bkb_dist_T = np.append(hky_from_bkb_dist_T, hky_from_bkb_dist)
            
            
            """
            To get single-season plots, comment in
            
            plt.scatter(*zip(*list(zip(hky_from_bkb_dist, hky_data_performance))))
            plt.title("Performance of  " + str(year) + " " + hky_tm + " by days ago " + bkb_tm + " played")
            plt.xlabel("Days ago " + bkb_tm + " played")
            plt.ylabel("Game Result")
            plt.show()

            
            plt.figure()
            fit_hky_for = np.polyfit(hky_from_bkb_dist, hky_goalsFor, deg=1)
            plt.plot(hky_from_bkb_dist, fit_hky_for[0] * hky_from_bkb_dist + fit_hky_for[1], color="blue")
            plt.scatter(*zip(*list(zip(hky_from_bkb_dist, hky_goalsAgainst))), label="Goals For", color="blue")
            
            fit_hky_against = np.polyfit(hky_from_bkb_dist, hky_goalsAgainst, deg=1)
            plt.plot(hky_from_bkb_dist, fit_hky_against[0] * hky_from_bkb_dist + fit_hky_against[1], color="red")
            plt.scatter(*zip(*list(zip(hky_from_bkb_dist, hky_goalsFor))), label="Goals Against", color="red")
            
            fit_hky = np.polyfit(hky_from_bkb_dist, hky_goals, deg=1)
            plt.plot(bkb_from_hky_dist, fit_hky[0] * bkb_from_hky_dist + fit_hky[1], label="Total Goals", color="black")
            
            plt.title("Goals scored in " + str(year) + " " + hky_tm + " games by days ago " + bkb_tm + " played")
            plt.xlabel("Days ago " + bkb_tm + " played")
            plt.ylabel("Goals")
            plt.legend(loc="upper right")
            plt.show()
        
            print("For: y = " + str(fit_hky_for[0]) + "x + " + str(fit_hky_for[1]))
            print("Against: y = " + str(fit_hky_against[0]) + "x + " + str(fit_hky_against[1]))
            print("Total: y = " + str(fit_hky[0]) + "x + " + str(fit_hky[1]))
            
            end of single-season hockey plots
            """
           
        plt.figure()
        fit_bkb_for_T = np.polyfit(bkb_from_hky_dist_T, bkb_pointsFor_T, deg=1)
        plt.plot(bkb_from_hky_dist_T, fit_bkb_for_T[0] * bkb_from_hky_dist_T + fit_bkb_for_T[1], color="blue")
        plt.scatter(*zip(*list(zip(bkb_from_hky_dist_T, bkb_pointsFor_T))), label="Points For", color="blue")
        
        fit_bkb_against_T = np.polyfit(bkb_from_hky_dist_T, bkb_pointsAgainst_T, deg=1)
        plt.plot(bkb_from_hky_dist_T, fit_bkb_against_T[0] * bkb_from_hky_dist_T + fit_bkb_against_T[1], color="red")
        plt.scatter(*zip(*list(zip(bkb_from_hky_dist_T, bkb_pointsAgainst_T))), label="Points Against", color="red")
        
        fit_bkb_T = np.polyfit(bkb_from_hky_dist_T, bkb_points_T, deg=1)
        plt.plot(bkb_from_hky_dist_T, fit_bkb_T[0] * bkb_from_hky_dist_T + fit_bkb_T[1], label="Total Points", color="black")
        
        plt.title("Points scored 2014-2017 in " + bkb_tm + " games by days ago " + hky_tm + " played")
        plt.xlabel("Days ago " + hky_tm + " played")
        plt.ylabel("Points")
        plt.legend(loc="upper right")
        plt.text(0, 40, "For: y = " + str(fit_bkb_for_T[0]) + "x + " + str(fit_bkb_for_T[1]))
        plt.text(0, 35, "Against: y = " + str(fit_bkb_against_T[0]) + "x + " + str(fit_bkb_against_T[1]))
        plt.text(0, 30, "Total: y = " + str(fit_bkb_T[0]) + "x + " + str(fit_bkb_T[1]))
        plt.show()
        
        plt.figure()
        fit_hky_for_T = np.polyfit(hky_from_bkb_dist_T, hky_goalsFor_T, deg=1)
        plt.plot(hky_from_bkb_dist_T, fit_hky_for_T[0] * hky_from_bkb_dist_T + fit_hky_for_T[1], color="blue")
        plt.scatter(*zip(*list(zip(hky_from_bkb_dist_T, hky_goalsAgainst_T))), label="Goals For", color="blue")
        
        fit_hky_against_T = np.polyfit(hky_from_bkb_dist_T, hky_goalsAgainst_T, deg=1)
        plt.plot(hky_from_bkb_dist_T, fit_hky_against_T[0] * hky_from_bkb_dist_T + fit_hky_against_T[1], color="red")
        plt.scatter(*zip(*list(zip(hky_from_bkb_dist_T, hky_goalsFor_T))), label="Goals Against", color="red")
        
        fit_hky_T = np.polyfit(hky_from_bkb_dist_T, hky_goals_T, deg=1)
        plt.plot(bkb_from_hky_dist_T, fit_hky_T[0] * bkb_from_hky_dist_T + fit_hky_T[1], label="Total Goals", color="black")
        
        plt.title("Goals scored 2014-2017 in " + hky_tm + " games by days ago " + bkb_tm + " played")
        plt.xlabel("Days ago " + bkb_tm + " played")
        plt.ylabel("Goals")
        plt.legend(loc="upper right")
        plt.text(0, -2.5, "For: y = " + str(fit_hky_for_T[0]) + "x + " + str(fit_hky_for_T[1]))
        plt.text(0, -3, "Against: y = " + str(fit_hky_against_T[0]) + "x + " + str(fit_hky_against_T[1]))
        plt.text(0, -3.5, "Total: y = " + str(fit_hky_T[0]) + "x + " + str(fit_hky_T[1]))
        plt.show()

        plt.figure()
        plt.scatter(*zip(*list(zip(bkb_from_hky_dist_T, bkb_data_performance_T))))
        plt.title("Performance of " + bkb_tm + " 2014-2017 by days ago " + hky_tm + " played")
        plt.xlabel("Days ago " + hky_tm + " played")
        plt.ylabel("Game Result")
        plt.show()
        
        plt.figure()
        plt.scatter(*zip(*list(zip(hky_from_bkb_dist_T, hky_data_performance_T))))
        plt.title("Performance of " + hky_tm + " 2014-2017 by days ago " + bkb_tm + " played")
        plt.xlabel("Days ago " + bkb_tm + " played")
        plt.ylabel("Game Result")
        plt.show()
        
    toc = time.time()
    print(str((toc-tic)*1000) + "ms")
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    