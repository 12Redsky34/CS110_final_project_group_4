# CS110_final_project_group_4
Repository for Final Project, CS110, Winter 2026

------

# Resume Reformatter
This program will take user information for a resume and reformat it into a text file to omit personal details that could contribute to bias for an employer to review.

# Overview
The user will input the following fields of information into the GUI: Name, Address, Contact(s), Work Experience, Education, and Skills. There is a "Preview" button that will allow the user to see what the program will ultimately output, allowing for transparency and the option to make edits to the provided information. Once the user is satisfied with their inputs, they will "Submit" their resume, upon which the program will output a .txt file. The output file will have personal information omitted for initial review stages by employers to minimize potential bias for or against certain applicants. Individuals (job-seekers, in this case) will typically send resumes to any relevant job listing and either hear nothing back at all or a simple rejection with no explanation. The intent with this program is to focus on the lack of transparency and equity in these modern models and at least allow applicants to preview exactly what an employer will see on their initial review, including which fields will be omitted, allowing for much better transparency and equity in the process.

# Background Research
Traditionally, individuals impacted the most in the market of job-seeking are those with marginalized or underprivileged backgrounds. Common markers used by employers to identify such groups are often tied to names and addresses, where certain kinds of names and certain areas are often tied to "underdeveloped" countries, upbringings, or locations. Even if an employer consciously does not want to attribute bias to any of these personal markers, unconscious bias is proven to still exert influence over decision making no matter the intent. Two applicants could have similar or near-identical qualifications and/or work experience, but one applicant with a name associated with marginalized groups will inevitably be chosen less over an individual that doesn't. One potential way to remove any possible bias from employer review is to simply omit personally identifying information of that nature, allowing them to make selections based only on education/work experience/etc upon which they can review personal information afterwards.
Another common issue with the application process is the lack of transparency. More often than not, a job-seeking individual will submit an application to a website only to have no idea what's being done with it, much less if it was ever looked at. Employers often never reach out with any decision made, acceptance, denial, or otherwise. Even when they do reach out to turn down an applicant, the reasons are often very generic or vague and do not give any insight into why the applicant was turned down, preventing them from improving their resume effectively for any future applications. We don't have a great answer for this problem, however we intend to allow for flexibility in what information the applicant can submit for employer review, as well as allowing the applicant to preview exactly what the data will look like to the reviewing employer, which is intended to increase transparency for this model.
Ideally, removing as much bias as possible and increasing transparency in the exchange of information would help increase the hiring rate of marginalized individuals, particularly those judged based only on name or location and the like, which would in turn prevent much of the detrimental effects of continual application rejections.

# Dependencies
This program requires Python 3.14.3+ to enable use of .removesuffix() attribute. Everything else used comes with any standard python installation.

# Configuration, Installation, Execution
Download the `gui.py` and `classes.py` files and save them to a convenient directory. To run the program, simply execute the `gui.py` file. `classes.py` is just a dependency. Upon submission of applicant information, a new text file will be saved to the `submissions` subdirectory. The program will create this directory if it does not already exist.

# Table of Files
| File name | Purpose | Contributor |
| ------    | ------  | ------      |
| gui.py | Graphical front end | Nate, Cordelia |
| classes.py | Utility classes | Nate, Cordelia |
| README.md | Readme file with all details about the program | Cordelia, Nate, Xindo|

# Citations
- Rinne, Ulf. “Anonymous Job Applications and Hiring Discrimination.” IZA World of Labor, IZA - Institute of Labor Economics., 22 Jan. 2025, wol.iza.org/articles/anonymous-job-applications-and-hiring-discrimination. 
- Dixon, Rebecca. “Anti-Discrimination - National Employment Law Project - Fighting Workplace Discrimination in All Its Form.” National Employment Law Project, NELP, 22 Aug. 2025, www.nelp.org/explore-the-issues/anti-discrimination/.
