-- displays the max temperature of each state (ordered by State name).

SELECT state, MAX(value) as max_temp from temperatures GROUP BY state;
