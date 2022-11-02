# Sunset color palette generator 

![example v1](assets/ss/example%20v1.png)

Example v1 app.


### The project has two parts
1) Experimentation, [experiments/](exp/), using Python.
    - Script to search Tweets with sunset picts.
    - Script to download sunsets pictures.
    - Unsupervised K-Means algorithm to sample representative color for each image of the dataset.
    - Unsupervised K-Means algorithm to generate final dataset with the most common colors.
2) Simple web as the final implementation.
    - Interactive sunset palette generator. It has two modes:
        - Default mode: Generate palettes using representative colors of all the dataset.
        - Creative modeo: Generate palettes using representative colors extracted from a single image.
    - Display information about sunsets.
    - Deployed using GitHub pages.

-----

### Contribute
Feel free to open an issue and maybe a Pull Request to suggest improvements :)


