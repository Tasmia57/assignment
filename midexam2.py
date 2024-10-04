n=int(input("Enter how many number you want to input:"))
input_scores=list(map(int,input(f"Enter {n} Number(coma separated):").split()))
max_score =max(input_scores)
print(f"Original Scores: {input_scores}")
print(f"Maximum Score: {max_score}")
avg=100/max_score
adjusted_scores = [score * avg for score in input_scores]
final_scores = [score if score >= 60 else 60 for score in adjusted_scores]
print(f"Final Scores: {[round(score, 2) for score in final_scores]}")





