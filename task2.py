def distribute_candies(ratings):
    n = len(ratings)
    candies = [1] * n

    # Left -> Right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right -> Left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


# Main program
ratings = eval(input("Enter ratings as a list: "))
print("Total candies needed:", distribute_candies(ratings))
