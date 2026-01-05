class ChaiUtils : 

    @staticmethod
    def clean_ingriedients(text) :
        return [item.strip() for item in text.split(",")]
    
raw = "  water, milk     ,   ginger,    sugar"

# obj = ChaiUtils()
# obj.clean_ingriedients(raw)
cleaned = ChaiUtils.clean_ingriedients(raw)
print(cleaned)