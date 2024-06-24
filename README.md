# rename.py

This is a simple script with a simple purpose: change the name of assignment submissions downloaded in bulk from [Gradescope][gradescope] to be the student ID number instead of the Gradescope submission number.

[gradescope]: https://gradescope.com

## Assumptions and prerequisites

1. You have Python 3+ and [pyyaml][pyyaml] installed on your computer. (On Arch Linux, pyyaml is provided by the package python-yaml.)
2. You have access to a terminal emulator on your computer.
3. You have a zip file containing a bulk download of assignment submissions from Gradescope.
4. You have unzipped above-mentioned zip file and have opened a terminal window and are in the directory with the contents of the zip file.
5. (Not really under your control) Gradescope has not changed the name or the internal structure of the metadata file `submission_metadata.yml`.

[pyyaml]: https://pyyaml.org

## What to do

If you have successfully verified assumptions 1-4 listed above, you proceed as follows.
(As for assumption 5, you'll know it is satisfied if all goes well.)

1. Clone this repository onto your computer, or simply [download only rename.py from this link][raw].
2. Copy the file `rename.py` into the directory with the contents of the zip file.
3. In the terminal and the directory with the contents of the zip file, run
```
python rename.py
```
This will print out the list of renaming operations as it is performing them.

At the end, all the pdf files in the directory should have names that look like `<studentid>.pdf` rather than the original `<submissionnumber>.pdf`.

That's all.

I tested this on a Linux machine.
The code is not using anything Linux-specific though, so it **should** work on anything capable of running Python.

[raw]: https://raw.githubusercontent.com/aghitza/gradescope-submissions-rename/master/rename.py
