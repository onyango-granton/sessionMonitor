package main

import (
	"log"
	"os"
	"regexp"
	"strings"
)

/*removes multiple whitespace with a single whitespace*/
func multispaceToSingleSpace(s string) string {
	multipleSpace := `\s+`
	pattern := regexp.MustCompile(multipleSpace)
	return pattern.ReplaceAllString(s, string(rune(32)))
}

func obtainEntryCred(s string) []string {
	singleSpacedEntry := multispaceToSingleSpace(s)

	//makes a list off space character
	entities := strings.Split(singleSpacedEntry, string(rune(32)))

	//filters out last two entries... or invalid entries
	if len(entities) < 8 {
		return nil
	}
	username := entities[0]
	logTime := entities[len(entities)-6:]

	// return username,Month,Date,Login,-,Logout,(TimeTaken)
	return append([]string{username}, logTime...)
}

func main() {
	//attempt to open user.txt generated
	userFile, err := os.ReadFile("dataManipulation/userLogFile/users.txt")

	//check for readFile error
	if err != nil {
		log.Fatalf(err.Error())
	}

	//gives us lpgins as per lines of entry
	fileEntries := strings.Split(string(userFile), string(rune(10)))

	//creating a csv file to hold data
	f, errf := os.OpenFile("clientOutput/data.csv", os.O_CREATE|os.O_WRONLY, 0644)

	//error handling for OpenFile csv
	if errf != nil {
		log.Fatalf(errf.Error())
	}

	defer f.Close()

	for _, ch := range fileEntries {
		//writing data to a csv file
		inputEntry := obtainEntryCred(ch)
		if inputEntry == nil {
			continue
		}

		//converting each entry into a comma seperated entry
		_, writeErr := f.WriteString(strings.Join(inputEntry, ",") + string(rune(10)))

		// error handling during csv file write
		if writeErr != nil {
			log.Fatalf(writeErr.Error())
		}

	}

}
