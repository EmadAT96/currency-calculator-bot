import os

from PIL import Image, ImageDraw, ImageFont

class CurrencyImageGenerator:
    
    POSITIONS = {
        "IRRTRY":  (205, 300),
        "IRREUR":  (700, 310),
        "IRRUSD":  (210, 480),
        "IRRAED":  (705, 480),
        "IRRCAD":  (205, 685),
        "IRRUSDT": (700, 685),
        "IRRGBP":  (205, 862),
    }
    
    
    TEXT_COLOR = "#123a66"    

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    def __init__ (
        self,
        template_path="../templates/currency_template.png",
        font_path="../fonts/Vazirmatn-Bold.ttf",
        font_size=40
    ):
        
        self.template_path =  os.path.join(self.BASE_DIR,template_path)
        self.font_path = os.path.join(self.BASE_DIR,font_path)
        self.font_size = font_size
        
    def format_amount(self,value: int) -> str:
        return f"{value:,}"
        
    def generate(
        self,
        rates,
        output_path
    ):
        
        output_path = os.path.join(self.BASE_DIR,output_path)
        
        image = Image.open(
            self.template_path
        )
        
        draw = ImageDraw.Draw(image)
        
        font = ImageFont.truetype(
            self.font_path,
            self.font_size
        )
        
        y = 100
        
        for rate in rates:
            
            name = rate.name
            
            value = rate.value
            
            if name not in self.POSITIONS:
                continue
            
            x, y = self.POSITIONS[name]
            
            text = self.format_amount(value)
            
            bbox = draw.textbbox((0, 0), text, font=font)
            
            th = bbox[3] - bbox[1]
            
            draw.text((x, y - th / 2 - bbox[1]), text, font=font, fill=self.TEXT_COLOR)
            
        image.save(
            output_path
        )
        
        return output_path