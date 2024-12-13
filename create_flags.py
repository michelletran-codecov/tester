

if __name__ == "__main__":

    flags = ""

    for i in range(1, 101):
        to_add = f"""
  flag_{i}:
    carryforward: true
    paths: 
      - app/{i}/*
"""
        flags += to_add


    print(flags)
