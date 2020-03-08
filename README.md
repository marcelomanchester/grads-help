# grads-help

## requires
    chocolatey = https://chocolatey.org/install

## install curl with chocolatey
    choco install curl

## import inpe's data
      git pull https://github.com/marcelomanchester/grads-help.git
      cd grads
      python importFiles.py
      
## genarete your own lon.txt, late.txt and prec.txt files with grads

## create your final.txt
      python createFiles.py
      
