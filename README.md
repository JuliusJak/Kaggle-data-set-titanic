# Kaggle-data-set-titanic
Data set uppgift. Titanic från kaggle. Använd machine learning för att förutse vem som överlever

Jag har använt mig av machine learning för att ta reda på en persons chans att överleva "The Titanic"
Jag har lyckats uåpnå en accuracy_scor på ca 81% genom att använda logistic regression

POSTMAN
använd dig utav localhost:5000/predict

Sedan i Body -> Raw -> JSON

inputa en persons information och få tillbaka ifall den personen överlevde eller inte
Exempel på input:
{
    "features": {
        "Pclass": 1,
        "Name": "miss jackson",
        "Sex": "female",
        "Age": 20,
        "SibSp": 0,
        "Parch": 1,
        "Fare": 7.2292,
        "Embarked": "c"
    }
}

Varför Logistic regression?

Anledningen till att jag valde logistic regression är för att jag kände att det var den metod som jag var bekvämast med och kunde prestera mest med.
Men jag tycker också att den är ett bra val.
1. LR är bra på binära problem vilket det här är. Did not Survived 0, Survived 1.
2. LR är även bra på att hantera Categorial features som "Sex" och "Embarked" 
och continuous features som "Age", "Fare" och "SibSp"
3. Det är även lätt att hantera tom data som finns det finns en del utav i denna data set
4. overfitting är lätt att undcvika med med LR

Men Det finns självklart andra metoder som kan få liknande resultat men det som slutgiltligen fick mig att bestämma vilken metod jag skulle använda var att jag behärskar LR bäst.


Dokumnetation av min process 
Efter att ha bestämt mig för vilket data set och vilken metod att använda så började jag med att ta reda på mer information om varje feature
jag gjorde det genom att göra diagram med Seaborn på de olika features. Detta gjorde så att jag kunde få en bra uppsikt av vad som var viktigt och vad som jag kunde exkludera.
Jag lärde mig att kvinnor hade en 74.2% överlenad medans men hade 18.9% överlevnad.
Från de olika diagramen kunde jag även dra slutsatsen att en persons status är av hög betydelse till en persons övelevnad
Jag kunde även se att en persons chans till övelevnad minskade destu fler syskon, partners eller familje medlemar man hade.

Sedan var det dags att konvertera features som inte var numeriska till numeriska värden. "Sex" och "Embarked" var lätt då jag kunde använda en labelmaker.
Det svåra var "Ticket", "Name" och "Cabin".
Min teori vid detta tillfälle vara att class och status hade störst påverkan till ens överlevnad föutom ens kön där kvinnor hade en betydligt högre chans att öveleva än män.
Så mitt mål var nu att kunna beräkna ut ens Status där jag skulle kunna jämföra ens status med ens överlevnad. 
Jag tänkte att jag skulle skriva en metod som kan värdera en persons status på en skala mellan 1-10 där 10 är den högsta möjliga status.
För att göra detta tänkte jag att man skulle kunna kombinera olika features från en person, features som "Pclass", "Name", "Ticket" och "Embarked".

Jag började med "Name" för att få en persons title, De vanligaste var "mr","miss" och "mrs". Detta var inte så hjälpsamt som jag hoppades men då det tillmesta del bara visar ifall en person är man och inte har en speciell titel eller ifall en kvinna utan speciell titel är gift.
jag byte då ens titel till numeriska värden. "mr", "miss", "mrs", "other" = 0,1,2,3
Efter att ha testat att lära min LR med och utan featuren "Name" visade det sig att accuracy skönk till ca 79,8% när jag inkluderade "Name"

Vid det här laget så hade jag inte mycket tid kvar till att experimentera så jag gjorde en metod för att kunna ta reda på vilken av alla features har störst påverkan på accuracy. Jag försökte göra en funktion som automatisk ger mig all olika kombinationer av features för att se de bästa och sämsta kombinationerna.
Jag kunde tyvärr inte fåden automatiska funktionen att fungera i tid.
Så jag tog beslutet att använda mig av drop() funktionen  för att ta bort "Tickets" och "Cabin" då jag inte hade tid att kovertera dem till numeriska värden. jag kunde även inte beräkna en persons status då jag inte hade tid och "Name" dropade jag då den endas minskade accuracy.
Detta betydde att jag använde mig av "Pclass", "Sex", "Age", SibSp", "parch", "Fare" och "Embarked" för att träna min LR.

Sen var det bara att göra min REST API.

Lite mer information till varje graf finns i 
