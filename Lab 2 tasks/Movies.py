movies = [ 
("Eternal Sunshine of the Spotless Mind", 20000000), 
("Memento", 9000000), 
("Requiem for a Dream", 4500000), 
("Pirates of the Caribbean: On Stranger Tides", 379000000), 
("Avengers: Age of Ultron", 365000000), 
("Avengers: Endgame", 356000000), 
("Incredibles 2", 200000000) 
]
sum_budgets = 0
high_budget_movies = []
for i in range(len(movies)): 
    sum_budgets += movies[i][1]
    avg = sum_budgets / len(movies)
print("Average movie budget is", avg)
for j in range(len(movies)):
    if movies[j][1] > avg:
        high_budget_movies.append(movies[j][0])
print("Movies with above average budgets are:", high_budget_movies)