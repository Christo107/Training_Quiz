# Training Evaluation Quiz
The purpose of this quiz is for Teachers/Trainers to evaluate whether the learners have a good grasp of the theory module concepts and contents that have been delivered to them previously. A link would be sent to the students for them to complete the 10 question quiz, and the name and final score is exported to a Google worksheet where the teacher can view and determine if the score is sufficient, or more training is required.

![Responsive Mockup](#)

The live website on Heroku can be accessed at the following link: [View my Live Website on Heroku here](https://progression-training-quiz.herokuapp.com/)

## CONTENTS

* [Introduction](#training-evaulation-quiz)

* [Features](#features)
    *  [Trainee Name Request](#trainee-name-request)
    *  [Introduction and Instructions](#introduction-and-instructions)
    *  []()
* [User Experience](#user-experience)
    *  [User Stories](#user-stories)
* [Design](#design)
    *  [Colour Palette](#colour-palette)
    *  [Typography](#typography)
    *  [Imagery](#imagery)
    *  [Wireframes](#wireframes)
    *  [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)   
    *  [Languages Used](#languages-used)
    *  [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Responsiveness Testing](#responsiveness-testing)
    * [Accessibility Testing](#accessibility-testing)
    * [User Story Testing](#user-story-testing)
    * [Bugs](#Bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Features

### Existing Sections
- #### **Trainee Name Request**
    - This initial input statement requests the trainee to enter their name to proceed.
    - If a name is not entered, a validation message appears informing them that a name is required to complete the quiz
    - Their name is then requested again
    - Once a name is entered, they move to the introduction and instruction section

![Trainee Name Request Image](./assets/documentation/images/trainee_name_request.jpg)
![Trainee Name Required Image](./assets/documentation/images/name_required.jpg)

- #### **Introduction and Instructions**
    - This section greets the trainee using the name they have entered previously to personalise the experience.
    - It outlines the following information to the user:
        - the amount of questions contained in the quiz,
        - the format of the questions,
        - the different options that can be chosen and
        - how to chose the option you want.
    - It then asks the user if they ready to proceed with the quiz
    
![Introduction and Instructions image](./assets/documentation/images/intro_instructions.jpg)

![](./assets/documentation/images)

- #### **Questions**
    - 

[](./assets/documentation/images/name_required.jpg)

### Future Features

## User Experience

### User Stories

#### Client Goals
- 
- 
- 
#### User Goals
- 
- 
- 
- 
-

## Design


### Wireframes
- I designed the website firstly through hand drawn sketches that were then turned into basic wireframes on Figma, before being made into high fidelity wireframes.

- [Desktop Wireframe](./assets/images/readme_images/wireframes/desktop_wireframe.png)
- [Tablet Wireframe](./assets/images/readme_images/wireframes/tablet_wireframe.png)
- [Mobile Wireframe](./assets/images/readme_images/wireframes/mobile_wireframe.png)
- [Desktop High Fidelity Wireframe](./assets/images/readme_images/wireframes/desktop_high_fidelity.png)
- [Tablet High Fidelity Wireframe](./assets/images/readme_images/wireframes/tablet_high_fidelity.png)
- [Mobile High Fidelity Wireframe](./assets/images/readme_images/wireframes/mobile_high_fidelity.png)



### Accessibility
- The website was designed and developed with accessibility in mind using colours that conform to the minimum 4.5:1 colour contrast ratio as per the WCAG 2.0 level AA Guidelines
- Semantic HTML elements allows for easier navigation of the website
- Alt text has been added to all non-decorative images used on the website
- Font style used is simple and easy to read for all users.

## Technologies used

### Languages used
- HTML5
- CSS3
- Javascript

### Frameworks, Libraries and Programs used
- [GitHub](https://github.com)
- [Gitpod](https://gitpod.io/workspaces)
- [Figma](https://www.figma.com/)
- [Optimizilla Image Compressor](https://imagecompressor.com)
- [Fontawesome](https://fontawesome.com/)
- [Am I Responsive](http://ami.responsivedesign.is/)
- [Coolers.co](https://coolors.co)
- [Chrome Dev Tools](https://www.google.com/intl/en_ie/chrome/)
- [A11y color contrast validator](https://color.a11y.com/Contrast/)
- [Favicon.io](https://favicon.io/)

## Testing
The website was tested for markup and CSS validation along with javascript, responsive design and accessibility using multiple browsers including Chrome, EDGE, and Firefox.
Please see screenshots of the results below:
- [W3C Markup Result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fchristo107.github.io%2FCI-PP-02-Rock_Paper_Scissors%2F) 
- [W3C CSS Validator Result](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fchristo107.github.io%2FCI-PP-02-Rock_Paper_Scissors%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

### Validator Testing
- HTML
    - Before final deployment, no errors were returned when passing through the offical W3C Validator
- CSS
    - Before final deployment, no errors were found when passing through the official W3C Jigsaw CSS Validator
- Javascript
    - The javascript code was run through jshint to check for any errors. Thankfully, no errors were identified.

### Responsiveness Testing
- The website was tested for responsiveness using the Chrome and Firefox browsers and their associated Developer Tools. 
#### Chrome
- A variety of screen sizes were checked for responsiveness using the Developer tools from 4K displays at 2560px wide, laptop sizes 1440px and 1024px, tablets at 768px, and a variety of mobile sizes down to 320px width. All elements maintained functionality and visibility in all scenarios, however, there were some issues with mobile landscape being able to fit all the componenets on the screen at the same time(see fixed bugs section below). Real world testing was also conducted on physical devices of various sizes to ensure integrity. No issue was encountered on these apart from the mobile landscape issue.
- A Lighthouse report was run several times to gauge the performance, accessibility, best practice and SEO scores. 

 - ![Lighthouse scoring Desktop](./assets/images/readme_images/lighthouse_report_desktop.png)
 - ![Lighthouse scoring Mobile](./assets/images/readme_images/lighthouse_report_mobile.png)

### Accessibility Testing
- Multiple tests were run on the website using Lighthouse and A11y Color Contrast Accessibility Validator to examine any accessibility issues. https://color.a11y.com/
#### Firefox
- Firefox's built in colour blindness simulator was used to identify any areas where sufficient colour contrast was not present. No such areas were found.

### User Story Testing
- I used the user stories to perform manual testing on the game to see whether there were any blockers to the user goals identified above. These are the results:

#### Client Goals
1. I want the game to be responsive so that is able to be played on multiple devices including laptops, tablets and mobile
    * The game was checked on multiple devices for responsiveness. There was an issue on small mobile devices where content overlapped but this was addressed and fixed. The game displays adequately on all size devices tested.
2. I want the game to be straightforward with clearly understandable instructions to avoid confusion
    * The game contains easy to understand instructions on how to start the game and how you win points. The instructions are displayed throughout the game for easy access.
3. I want the game to be accessible to all with clear text, imagery and image descriptions where appropriate
    * The font, imagery and layout provide the user with a clean and ncluttered interface in which to play the game. alt tags have been added to images, and the colours used exceed the requirements for colour contrast as confirmed by tests performed on A11y.com website checker.
    
#### User Goals
1. As a User I want to know what the game is when I first arrive on the site so I can decide if I want to play
    * The clear game title at the top of the page and example imagery present in the game area demonstrates what the game is and what it will involve
2. As a User I want be able to read the rules of the game easily so I understand what I have to do to play
    * The game rules section underneath the controls area are visible all the time so the user is able to read and understand them before and while playing
3. As a User I want to know how to start the game so I can enjoy playing
    * The instruction message above the controls area shows the user how to start the game by choosing one of the options
4. As a User I want to be able to reset the game at any point so I can try again to win
    * Once the game commences, a restart button appears in the centre of the screen to be cearly visible and easiliy accessible for the user to restart the game at any point.
5. As a User I want to be able to exit the game at any point when I have played enough
     * There are no blockers for the user to exit the game at any point. There are no popups to dissuade the user from leaving when they choose to do so.

## Deployment
I used Gitpod to develop the website and the site was deployed using GitHub Pages. Please see details below:

- The steps to deploy are as follows: 
    - In the GitHub repository (https://github.com/Christo107/CI-PP-02-Rock_Paper_Scissors), navigate to the Settings tab 
    - On the left hand side, locate the Pages section
    - From the source section drop-down menu, select the main branch and save
    - Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

- It can also be forked via the following steps:
    - Log in to GitHub and locate the repository again, as described above.
    - At the top right corner of the repository, you will see a "Fork" button. Click on it.
    - You will then be asked where you want to save it, so choose a location.
    - You now should have a copy of this repository in your own GitHub account.


The live link can be found here - https://christo107.github.io/CI-PP-02-Rock_Paper_Scissors/

## Bugs
### Fixed Bugs
- Overlapping Content Bug: This bug appeared on small mobile devices where the computer choice area was overlapping the controls area. This was fixed by adjusting the margin of the controls area to position it further down the page.
    * [Overlapping Content Bug](./assets/images/bugs/overlapping_%20content_bug.png)
- GameOver modal was not appearing when either the player or computer reached the maximum 10 points. The cause was identified as the function was being called in the wrong place. The gameover modal now displays as below:
    * [Winning Game Over Modal Image](./assets/images/readme_images/win_game_modal.png)
- On mobile landscape, there were issues around fitting all elements on the screen. A media query specifically for mobile landscape was added to fix this issue, however some styling issues remain which will be fixed in future releases.
    * [Mobile Landscape Bug](./assets/images/bugs/mobile_landscape_bug.jpg)
    * [Mobile Landscape Bug Fixed](./assets/images/bugs/mobile_landscape_bug_fixed.jpg)

### Known Bugs
- Styling issues on mobile landscape

## Credits

### Code

- Some game javascript code was based on Code Institute's Rock Paper Scissors example. See code comments for details of which code segments this applies to.
- Some game javascript code was based on Code Institute's Love Maths example. See code comments for details of which code segments this applies to.
- Several tutorials on developing a Rock Paper Scissors game were viewed but no code was used directly from these tutorials and were used solely for inspiration on how to implement the game. The tutorials were as follows:
    * Web Dev Simplified https://www.youtube.com/watch?v=1yS-JV4fWqY
    * Code with Ania Kubow https://www.youtube.com/watch?v=RwFeg0cEZvQ

### Content

- The text content of the website was written by the developer.
- The social media icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The imagery used in the game was taken from (https://www.pinclipart.com/) and is free to use.

## Acknowledgements
 - The CI students who peer reviewed my website and gave feedback
 - Daniel Maher on his assistance with a problem I encountered.