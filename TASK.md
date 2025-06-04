This is the task description for the project.
Read this to generate code for the project.

# Project Name
`Xlt wash-ocr`

# Project Language
+ VUE3
+ JAVASCRIPT
+ Html+Css
+ Python
+ Flask

# Overall Project Description
This project contains two parts:
+ Back-end part: using python to generate a flask server.
+ Front-end part: using VUE3 to create a project.
Front-end part is opened from browser by user, given the `taskid`, and it calls the `back-end part` to get the details of the `taskid`, and then render the webpage.

## Back-end part
+ Using python to generate a flask server: `http://localhost:5000/taskid`.
+ The return json is:
```
{

    taskID: "xxxx",
    car-id: "1122",
    begintime: 1702060386,
    endtime: 1702060386,
    carrages: 12,
    details: [
        {
            "carrage-id": "01",
            "image": ["01-A","01-B.jpg"]
            "score": [0.8,0.2]
        },
        {
            "carrage-id": "02",
            "image": ["02-A","02-B.jpg"]
            "score": [0.8,0.2]
        },
        // 3-11 carrages information...
        {
            "carrage-id": "12",
            "image": ["12-A","12-B.jpg"]
            "score": [0.8,0.2]
        }
    ]
}
```
Suppose the `images` defines the path of the images, and the `score` defines the score of the images.


## Front-end part
Using VUE3 to create a project:
+ It will display a simple text "Xlt wash-ocr is running" when user open `http://localhost`, to indicate that the project is running.
+ It will display a webpage when user open `http://localhost/taskid`, which `taskid` is given by the user. This page is the only page of the project.
+ Before rendering the webpage, it first calls the `api` above to get the details of the `taskid`, and then render the webpage.

Webpage Content is as follows:
+ This page size is 800px-width and 500px-height.
+ Page title is the given `taskID`, centered in the page.
+ Below, there is a array of buttons, each button is a `carrage-id`, and the buttons are centered in the page. When user click a button, it will display the corresponding image of the item  in the `details` array.
+ Below, there displays two images `img-A.jpg` and `img-B.jpg` horizontally aligned, of which the path is get from the user clicked button.
+ Below, there is a `Text Area` to display the `score` of the corresponding `carrage-id`.
+ Note: the images are clickable, display a big image page to view the image.
