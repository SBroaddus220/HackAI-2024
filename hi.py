import requests

def main():
    r = requests.get("https://www.google.com/")
    print(r.text)
    
if __name__ == "__main__":
    main
    print("Hello World")