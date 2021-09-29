# Lab 3 Report

## Smart and Healthy Buildings

## 9/29/21

Alden Summerville, Aparna Kishore

ads3pu, ak8mj

### Public Github repo

aparnakishore/[smart-buildings](https://github.com/aparnakishore/smart-buildings-lab3)

### Plans

- (Alden) Create public repo to share our work

- (Alden+Aparna) Create a "generatelinklabheatmap" function with arguments:startdatetime, enddatetime, fields, exportfilepath

- (Alden+Aparna) Iterate over a range of 200 to account for each grid point(however, not every grid point will have sensor data -- simple if, else)

- (Alden+Aparna) Initialize empty counter and array.  For each grid point,iterate over the fields passed to the function

- (Alden+Aparna) Pull the sensor data using the ’getlfdf’ fxn from the utilitymodule.  Calculate the length of that resulting df, and add it to the counter

- (Alden+Aparna) Create an array from the resulting counter and append itto the original empty array

- (Aparna) After the iterations, reshape the final array to size 10,20 tomatch the living link lab grid image

- (Aparna) Next, take the log of the array in order to handle the large rangeof values and provide a more informative heatmap

- (Aparna) Use the seaborn package to create the heatmap, and use the ’heatmap.imshow’(image show) functionality to print the grid image behind the heatmap

- (Aparna) Finally, export the heatmap as an image using the file path passedby the user

- (Alden) Next, create a main function (called in the main block) that asksthe for users input for each heatmap fxn parameters, then runs the heatmapfunction

- (Alden) Generate a latex report detailing the process of the lab3.Heatmap Function:
