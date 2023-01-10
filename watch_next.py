# Compulsory Task 2 of T38.
import spacy


# Define a function to get movies description from the file.
def read_file():
    # define a list to store the movies description.
    movies_list = []
    
    fr = None
    try:
        fr = open("movies.txt", "r")
        for line in fr:
            movies_list.append(line)
    except FileNotFoundError:
        print("File not found!")
    finally:
        if fr != None:
            fr.close

    if len(movies_list)>0:
        return movies_list
    else:
        return None    


# Define a funciton to return which movies a user would watch next time.
# Parameter is description of movie.
# Return is title of movie.
def find_movie(descrpt):
    title = ""
    descrption = ""
    similarity = 0.0
    
    # Get movies list.    
    movies_list = read_file()

    # Find out the movie which the most similarity.
    if len(movies_list) > 0:
        score = 0.0
        nlp = spacy.load('en_core_web_md') 
        model_sentence = nlp(descrpt)

        for sentence in movies_list:
            split = sentence.split(":")
            # title = split[0]
            score = nlp(split[1]).similarity(model_sentence)
            # print(sentence + " - ", score)
            if similarity == 0:
                similarity = score
                title = split[0]
                descrption = split[1]
            else:
                if score > similarity:
                    similarity = score
                    title = split[0]
                    descrption = split[1]
    else:
        print("No found movies description.")

    return title, descrption


# Define a function to get message from user.
def input_message(subject):
    in_message = ""
    while len(in_message) == 0:
        in_message = input(subject)
    return in_message


# Define a main function entry.
def main():
    movie_descrp = input_message("\nPlease input the description of movie you have watched: ")
    movie_title, movie_descrpt = find_movie(movie_descrp)
    if len(movie_title) > 0:
        print(f"\nAccording to you description of you have watched movie, we recommend movie '{movie_title}' for you watch.")
        print(f"The movie description is: {movie_descrpt}\n")
    else:
        print("\nNo suitable movie found for you watch.")


if __name__ == '__main__':
    main()

