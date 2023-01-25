def main()->None:
   #/* Step 1: Read three numbers */
    a, b, c = input("Enter three numbers: ").split()
   #/* Step 2: Find the median number */
    if (a >= b): 
        if (b <= c):
            if a>= c:
                m = c
            else: 
                m = a
        else:
            m = b
    else:
        if (b >= c):
            if a <= c:
                m = c
            else:
                m = a
        else:
            m = b
   #/* Step 2: Print the median number */
    print("Median number is: ", m)
if __name__ == "__main__":
    main()