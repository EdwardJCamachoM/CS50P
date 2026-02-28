def main():
    file = input("File name: ").lower().strip()

    if ".gif" in file:
        print("image/gif")
    elif ".jpg" in file:
        print("image/jpg")
    elif ".jpeg" in file:
        print("image/jpeg")
    elif ".png" in file:
        print("image/png")
    elif ".pdf" in file:
        print("document/pdf")
    elif ".txt" in file:
        print("text/plain")
    elif ".zip" in file:
        print("application/zip")
    else:
        print("application/octet-stream")

main()