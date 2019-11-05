import os
def pyMerger(directory):
    pdfFiles = [f for f in os.listdir(directory) if f.lower().endswith("pdf")]
    merger = PdfFileMerger()

    if pdfFiles != []:  # check if directory has pdf files in it
        for filename in pdfFiles:
            if filename != "_mergedFull.pdf":  # check if merged file already exists and skip it
                merger.append(PdfFileReader(os.path.join(directory, filename), "rb"))

        outputFile = os.path.join(r'c:\pdf', directory+"_mergedFull.pdf")
        merger.write(outputFile)  # it will overwrite if final file existed
    else:
        print(directory + " has no pdf files in it.")

