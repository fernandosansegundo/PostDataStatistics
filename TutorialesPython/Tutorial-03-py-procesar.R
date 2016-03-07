library(knitr)

OSystem = R.version$platform
# ipythonStatus = attr(system2(command = "ipython3", args = "--version", stderr = TRUE, stdout = NULL), "status")
# pythonStatus = system2(command = "python3", args = "--version", stderr = TRUE, stdout = NULL), "status")

Mac = grepl("apple", OSystem)
Windows = grepl("w64|w32", OSystem)

if(Mac){
  pythonCommnd = "python3"
}
if(Windows){
  pythonCommnd = "ipython3"
}





DeMere1 = TRUE
purl("Tutorial-03-py.Rnw", output = "./code/Tut-03-DeMere01.py", documentation = FALSE)
system2(command = pythonCommnd, args="./code/Tut-03-DeMere01.py", stdout = "./code/Tut-03-DeMere01.out")
DeMere1 = FALSE

probGeom1 = TRUE
purl("Tutorial-03-py.Rnw", output = "./code/Tut-03-probGeom1.py", documentation = FALSE)
#pythonOut = system("ipython3 ./code/Tut-03-probGeom1.py", intern = TRUE)
#writeLines(pythonOut, con="./code/Tut-03-probGeom1.out")
system2(command = pythonCommnd, args="./code/Tut-03-probGeom1.py", stdout = "./code/Tut-03-probGeom1.out")
probGeom1 = FALSE
