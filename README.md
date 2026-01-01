# Research Paper Reader for Mobile
A mobile app for reading research papers on mobile phones with small screens 

## Related Works
**Adobe Acrobat Reader**  
Has "Liquid Mode" feature, making general PDFs mobile-friendly to read. However, it does not give the option to change the font size nor consider text breaks common to research papers with multiple columns of text. 

**Zotero**  
Has a "Full Text" feature that extracts all the text in the PDF and combines it in a mobile-friendly view. However, the texts extracted does not differentiate between sections (tables, figures, main body, footnotes, etc.) and equations. 

## Pipeline
**1. Data Extractor**  
Given a PDF file or Latex files of the research paper, it will convert them into formatted data for the app to organize into a mobile-friendly view.

**2. Mobile Viewer**  
Reads the formatted data and organizes it into a mobile-friendly view. The user should be able to modify the view to make it more personalized and readable.

## Current Status
So cooked rn. 

Currently experimenting data extractor ideas in python.

## Ideal Solution
The pipeline is ran entirely on mobile

## Current Realistic Solution
PDF Extractor is ran on a desktop PC or server, and the formatted data is sent and saved to mobile for viewing. 
