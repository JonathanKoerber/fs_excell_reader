# FS ExCell Reader

The program will take a excell workbook and read the FS menu excell workbook and creae json menu objects by meal. 
Objects will look as follows:

```json
{
    prep-date: <mm/dd/yyyy>,
    consume-date: <mm/dd/yyy>,
    meal: <Lunch, Dinner>, 
    meal-type: <Regular || CM || Veg || Kids || etc >,
    total-portion: <int>,
    ingredients:[
        {name: <text>, 
        portion-by: <'pc' || 'weight'>,
        source: <inhouse||bought>,
        directions: <text>
        ingredients:[
            {amount: <int>,
            unit: <lbs||oz>
            name: <text>,
            prep: <text>
            }
        ]
        }
    ]
    instructions: <text>
}
```