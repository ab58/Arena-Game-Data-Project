Arena Game Data Project (NHL and NBA teams with shared arenas)

This is my first foray into data analysis with python, in particular with using matplotlib and pandas.

QUESTION

For NHL and NBA teams that share arenas, does how recently the other team played in the arena affect the performance/outcome of 
a team's game? For example, does a team tend to score less or lose more if the other sport's team played in that arena the previous day or 
2, compared to if they played 4-5 days ago or more? This is a common grievance among fans of both leagues, and it has occasionally been 
suspected by fans that the arena having been restructured and re-purposed in such a short timespan affects the quality or playing 
conditions for the next game of the other sport held in the arena. Restructuring and Re-purposing on such short notice is said to affect ice quality and/or court quality, as well as physical differences required such as heat or ventilation.

8 pairs of teams are examined in this project (Philadelphia 76ers/Flyers, Denver Nuggets/Colorado Avalanche, Chicago Bulls/Blackhawks,
Boston Celtics/Bruins, Washington Wizards/Capitals, New York Knicks/Rangers, Toronto Raptors/Maple Leafs, Dallas Mavericks/Stars). Data  
on the Los Angeles Clippers, Lakers and Kings are also available, but since this is a triplet instead of a pair, they have been left out of
the analysis for the time being (this may change in the future though). Data are gathered from the sports-reference.com network, in 
particular the websites:

https://www.backetball-reference.com/

https://www.hockey-reference.com/

Data are from the last 4 full seasons played at the time of this project: 2013-14, 2014-15 2015-16, and 2016-17. The object of the 
analysis is to find, for each team in each year, any correlation between the number of "days ago" the arena's other team played, and plot 
that against the team's scoring for and against, as well as the game outcomes. For example, the Flyers' game results will be plotted 
against the number of "days ago" the 76ers played in that arena (i.e. the most recent game before the Flyers' home game), the Bulls' game 
results are plotted against the number of days ago the Blackhawks played their most recent home game, and likewise for each NBA-NHL team 
pairing. 

At the end, data are plotted in matplotlib for each team over the 4 years, showing goals/points for (blue line), goals/points against (red 
line) and total goals (black line) compared to how recently the arena's other team played (measured by days ago). A second plot for each 
team in each year shows the game results (for basketball, Win/Loss shown as 1 and 0, for hockey, Win/OT/Loss shown as 2, 1 and 0) 
compared to how recently the other team played in the arena. Data can be observed by running the code with all the data in the folder 
arena-home-data, which needs to be passed as an argument to the script.

By default, the code prints only the cumulative 4-season plots for each team. There are commented out code blocks to get the single-season 
plots for each team, one each for the hockey and basketball teams. The lines to comment in or out depending on if single-season plots are 
desired are shown in the script.

Hope you enjoy this little pet project! This was really a practice exercise to familiarize myself with the data science toolbox available 
in python and its versatility. Nonetheless I came up with meaningful data visualizations and got an opportunity to explore and attempt to 
answer a question which greatly interests me as a sports fan, and address this longstanding fan grievance once and for all!