import scrapy

MAPEO_NOMBRES_ELCANO = {
    # Canales satélite
    "La1": "La 1 HD",
    "La1 UHD": "La 1 UHD",
    "La2": "La 2",
    "tdp 1080": "Teledeporte",
    "GOL TV 1080": "GOL PLAY 1080",
    "CUATRO 1080": "Cuatro 1080",
    "Telecinco 1080": "Telecinco 1080",
    "BeMad 1080": "Be Mad 1080",
    # Canales LaLiga
    "M. LaLiga UHD": "M+ LaLiga TV UHD 1080",
    "M. LaLiga 1080P": "M+ LaLiga TV 1080",
    "M. LaLiga 1080 MultiAudio": "M+ LaLiga TV 1080",
    "M. LaLiga 720": "M+ LaLiga TV HD",
    "M. LaLiga 2 1080": "M+ LaLiga TV 2 1080",
    "M. LaLiga 2 720": "M+ LaLiga TV 2 HD",
    "M. LaLiga 3 1080": "M+ LaLiga TV 3 1080",
    "La Liga BAR 1080": "LaLiga TV BAR 1080",
    "DAZN LaLiga 1080 MultiAudio": "DAZN LaLiga 1080",
    "DAZN LaLiga 720": "DAZN LaLiga HD",
    "DAZN LaLiga 2 1080 MultiAudio": "DAZN LaLiga 2 1080",
    "DAZN LaLiga 2 720 MultiAudio": "DAZN LaLiga 2 HD",
    # Canales LaLiga Hypermotion
    "LaLiga Smartbank 1080": "LaLiga TV Hypermotion 1080",
    "LaLiga Smartbank 720": "LaLiga TV Hypermotion HD",
    "LaLiga Smartbank 2 1080": "LaLiga TV Hypermotion 2 1080",
    "LaLiga Smartbank 2 720": "LaLiga TV Hypermotion 2 HD",
    "LaLiga Smartbank 3": "LaLiga TV Hypermotion 3 1080",
    # Canales Champions League
    "M.L. Campeones 1080 MultiAudio": "M+ Liga de Campeones 1080",
    "M.L. Campeones 1080P": "M+ Liga de Campeones 1080",
    "M.L. Campeones 720": "M+ Liga de Campeones HD",
    "M.L. Campeones 2 1080": "M+ Liga de Campeones 2 1080",
    "M.L. Campeones 2 720": "M+ Liga de Campeones 2 HD",
    "M.L. Campeones 3 1080": "M+ Liga de Campeones 3 1080",
    "M.L. Campeones 3 720": "M+ Liga de Campeones 3 HD",
    "M.L. Campeones 4 1080": "M+ Liga de Campeones 4 1080",
    "M.L. Campeones 5 1080": "M+ Liga de Campeones 5 1080",
    "M.L. Campeones 6 1080": "M+ Liga de Campeones 6 1080",
    "M.L. Campeones 7 1080": "M+ Liga de Campeones 7 1080",
    "M.L. Campeones 8 1080": "M+ Liga de Campeones 8 1080",
    "M.L. Campeones 9 SD": "M+ Liga de Campeones 9 SD",
    "M.L. Campeones 10 SD": "M+ Liga de Campeones 10 SD",
    "M.L. Campeones 11 SD": "M+ Liga de Campeones 11 SD",
    "M.L. Campeones 12 SD": "M+ Liga de Campeones 12 SD",
    "M.L. Campeones 13 SD": "M+ Liga de Campeones 13 SD",
    # Canales Fórmula 1
    "DAZN F1 Multicamara (Fórmula 1)": "DAZN F1 1080",
    "DAZN F1 1080 (Fórmula 1)": "DAZN F1 1080",
    "DAZN F1 1080 (Fórmula 1)": "DAZN F1 1080",
    "DAZN F1 720 (Fórmula 1)": "DAZN F1 HD",
    # Canales Golf
    "M. Golf 1080": "M+ Golf 1080",
    "M. Golf2 1080": "M+ Golf 2 1080",
    # Canales Eurosport
    "Eurosport4k": "Eurosport 1 UHD",
    "EuroSport 1 1080": "Eurosport 1 1080",
    "EuroSport 2 1080": "Eurosport 2 1080",
    # Otros canales
    "M.Plus 1080": "Movistar Plus+ 1080",
    "M. Deportes 1080": "M+ Deportes 1080",
    "M. Deportes 720": "M+ Deportes HD",
    "M. Deportes 2 1080": "M+ Deportes 2 1080",
    "M. Deportes 3 1080": "M+ Deportes 3 1080",
    "M. Deportes 4 1080": "M+ Deportes 4 1080",
    "M. Deportes 5 1080": "M+ Deportes 5 1080",
    "M. Deportes 6 1080": "M+ Deportes 6 1080",
    "M. Deportes 7 1080": "M+ Deportes 7 1080",
    "Barça 720": "Barcelona TV HD",
}

MAPEO_NOMBRES_ROBERTOFREIJO = {
    # Canales satélite
    "La 1 HD": "La 1 HD",
    "La 1 UHD": "La 1 UHD",
    "La 2": "La 2",
    "tdp 1080p": "Teledeporte",
    "GOL TV 1080p": "GOL PLAY 1080",
    "CUATRO 1080p": "Cuatro 1080",
    "Telecinco 1080p": "Telecinco 1080",
    "BeMad 1080p": "Be Mad 1080",
    # Canales LaLiga
    "M. LaLiga 4K": "M+ LaLiga TV UHD 1080",
    "M. LaLiga 1080p": "M+ LaLiga TV 1080",
    "M. LaLiga 1080p MultiAudio": "M+ LaLiga TV 1080",
    "M. LaLiga 720p": "M+ LaLiga TV HD",
    "M. LaLiga 2 1080p": "M+ LaLiga TV 2 1080",
    "M. LaLiga 2 720p": "M+ LaLiga TV 2 HD",
    "M. LaLiga 3 1080p": "M+ LaLiga TV 3 1080",
    "La Liga BAR 1080p": "LaLiga TV BAR 1080",
    "DAZN LaLiga 1080p MultiAudio": "DAZN LaLiga 1080",
    "DAZN LaLiga 720p": "DAZN LaLiga HD",
    "DAZN LaLiga 2 1080p MultiAudio": "DAZN LaLiga 2 1080",
    "DAZN LaLiga 2 720p MultiAudio": "DAZN LaLiga 2 HD",
    # Canales LaLiga Hypermotion
    "LaLiga Smartbank 1080p": "LaLiga TV Hypermotion 1080",
    "LaLiga Smartbank 720p": "LaLiga TV Hypermotion HD",
    "LaLiga Smartbank 2 1080p": "LaLiga TV Hypermotion 2 1080",
    "LaLiga Smartbank 2 720p": "LaLiga TV Hypermotion 2 HD",
    "LaLiga Smartbank 3": "LaLiga TV Hypermotion 3 1080",
    # Canales Champions League
    "M.L. Campeones 1080p MultiAudio": "M+ Liga de Campeones 1080",
    "M.L. Campeones 1080p": "M+ Liga de Campeones 1080",
    "M.L. Campeones 720p": "M+ Liga de Campeones HD",
    "M.L. Campeones 2 1080p": "M+ Liga de Campeones 2 1080",
    "M.L. Campeones 2 720p": "M+ Liga de Campeones 2 HD",
    "M.L. Campeones 3 1080p": "M+ Liga de Campeones 3 1080",
    "M.L. Campeones 3 720p": "M+ Liga de Campeones 3 HD",
    "M.L. Campeones 4 1080p": "M+ Liga de Campeones 4 1080",
    "M.L. Campeones 5 1080p": "M+ Liga de Campeones 5 1080",
    "M.L. Campeones 6 1080p": "M+ Liga de Campeones 6 1080",
    "M.L. Campeones 7 1080p": "M+ Liga de Campeones 7 1080",
    "M.L. Campeones 8 1080p": "M+ Liga de Campeones 8 1080",
    "M.L. Campeones 9 SD": "M+ Liga de Campeones 9 SD",
    "M.L. Campeones 10 SD": "M+ Liga de Campeones 10 SD",
    "M.L. Campeones 11 SD": "M+ Liga de Campeones 11 SD",
    "M.L. Campeones 12 SD": "M+ Liga de Campeones 12 SD",
    "M.L. Campeones 13 SD": "M+ Liga de Campeones 13 SD",
    # Canales Fórmula 1
    "DAZN F1 Multicamara (Fórmula 1)": "DAZN F1 1080",
    "DAZN F1 UHD (Fórmula 1)": "DAZN F1 UHD",
    "DAZN F1 1080p (Fórmula 1)": "DAZN F1 1080",
    "DAZN F1 720p (Fórmula 1)": "DAZN F1 HD",
    # Canales Golf
    "M. Golf 1080p": "M+ Golf 1080",
    "M. Golf2 1080p": "M+ Golf 2 1080",
    # Canales Eurosport
    "Eurosport4k": "Eurosport 1 UHD",
    "EuroSport 1 1080p": "Eurosport 1 1080",
    "EuroSport 2 1080p": "Eurosport 2 1080",
    # Otros canales
    "M.Plus 1080p": "Movistar Plus+ 1080",
    "M. Deportes 1080p": "M+ Deportes 1080",
    "M. Deportes 720p": "M+ Deportes HD",
    "M. Deportes 2 1080p": "M+ Deportes 2 1080",
    "M. Deportes 3 1080p": "M+ Deportes 3 1080",
    "M. Deportes 4 1080p": "M+ Deportes 4 1080",
    "M. Deportes 5 1080p": "M+ Deportes 5 1080",
    "M. Deportes 6 1080p": "M+ Deportes 6 1080",
    "M. Deportes 7 1080p": "M+ Deportes 7 1080",
    "Barça 720p": "Barcelona TV HD",
    "Real Madrid TV 1080p": "Real Madrid TV 1080",
    "Real Madrid TV 720p": "Real Madrid TV HD",
    "Onetoro HD": "Onetoro HD",
}

MAPEO_IDS = {
    # Canales satélite
    "La 1 HD": "La 1 HD",
    "La1 UHD": "La 1 HD",
    "La 2": "La 2",
    "Teledeporte": "Teledeporte",
    "GOL PLAY 1080": "GOL PLAY",
    "Cuatro 1080": "Cuatro HD",
    "Telecinco 1080": "Telecinco HD",
    "Be Mad 1080": "Be Mad",
    # Canales LaLiga
    "M+ LaLiga TV UHD 1080": "M+ LaLiga TV UHD",
    "M+ LaLiga TV 1080": "M+ LaLiga TV HD",
    "M+ LaLiga TV HD": "M+ LaLiga TV HD",
    "M+ LaLiga TV 2 1080": "M+ LaLiga TV 2 HD",
    "M+ LaLiga TV 2 HD": "M+ LaLiga TV 2 HD",
    "M+ LaLiga TV 3 1080": "M+ LaLiga TV 3 HD",
    "LaLiga TV BAR 1080": "LaLiga TV BAR HD",
    "DAZN LaLiga 1080": "DAZN LaLiga HD",
    "DAZN LaLiga HD": "DAZN LaLiga HD",
    "DAZN LaLiga 2 1080": "DAZN LaLiga 2 HD",
    "DAZN LaLiga 2 HD": "DAZN LaLiga 2 HD",
    # Canales LaLiga Hypermotion
    "LaLiga TV Hypermotion 1080": "LaLiga TV Hypermotion HD",
    "LaLiga TV Hypermotion HD": "LaLiga TV Hypermotion HD",
    "LaLiga TV Hypermotion 2 1080": "LaLiga TV Hypermotion 2",
    "LaLiga TV Hypermotion 2 HD": "LaLiga TV Hypermotion 2",
    "LaLiga TV Hypermotion 3 1080": "LaLiga TV Hypermotion 3",
    # Canales Champions League
    "M+ Liga de Campeones 1080": "M+ Liga de Campeones HD",
    "M+ Liga de Campeones HD": "M+ Liga de Campeones HD",
    "M+ Liga de Campeones 2 1080": "M+ Liga de Campeones 2 HD",
    "M+ Liga de Campeones 2 HD": "M+ Liga de Campeones 2 HD",
    "M+ Liga de Campeones 3 1080": "M+ Liga de Campeones 3 HD",
    "M+ Liga de Campeones 3 HD": "M+ Liga de Campeones 3 HD",
    "M+ Liga de Campeones 4 1080": "M+ Liga de Campeones 4",
    "M+ Liga de Campeones 5 1080": "M+ Liga de Campeones 5",
    "M+ Liga de Campeones 6 1080": "M+ Liga de Campeones 6",
    "M+ Liga de Campeones 7 1080": "M+ Liga de Campeones 7",
    "M+ Liga de Campeones 8 1080": "M+ Liga de Campeones 8",
    "M+ Liga de Campeones 9 SD": "M+ Liga de Campeones 9",
    "M+ Liga de Campeones 10 SD": "M+ Liga de Campeones 10",
    "M+ Liga de Campeones 11 SD": "M+ Liga de Campeones 11",
    "M+ Liga de Campeones 12 SD": "M+ Liga de Campeones 12",
    "M+ Liga de Campeones 13 SD": "M+ Liga de Campeones 13",
    # Canales Fórmula 1
    "DAZN F1 1080": "DAZN F1 HD",
    "DAZN F1 HD": "DAZN F1 HD",
    # Canales Golf
    "M+ Golf 1080": "M+ Golf HD",
    "M+ Golf 2 1080": "M+ Golf 2 HD",
    # Canales Eurosport
    "Eurosport 1 UHD": "Eurosport 1 HD",
    "Eurosport 1 1080": "Eurosport 1 HD",
    "Eurosport 2 1080": "Eurosport 2 HD",
    # Otros canales
    "Movistar Plus+ 1080": "Movistar Plus+ HD",
    "M+ Deportes 1080": "M+ Deportes HD",
    "M+ Deportes HD": "M+ Deportes HD",
    "M+ Deportes 2 1080": "M+ Deportes 2 HD",
    "M+ Deportes 3 1080": "M+ Deportes 3",
    "M+ Deportes 4 1080": "M+ Deportes 4",
    "M+ Deportes 5 1080": "M+ Deportes 5",
    "M+ Deportes 6 1080": "M+ Deportes 6",
    "M+ Deportes 7 1080": "M+ Deportes 7",
    "Barcelona TV HD": "Barcelona TV",
    "Real Madrid TV 1080": "Real Madrid TV",
    "Real Madrid TV HD": "Real Madrid TV",
    "Onetoro HD": "Onetoro",
}

MAPEO_LOGOS = {
    # Canales satélite
    "La 1 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/La%201.png",
    "La 1 UHD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/La%201.png",
    "La 2": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/La%202.png",
    "Teledeporte": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Teledeporte.png",
    "GOL PLAY": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/GOL%20PLAY.png",
    "Cuatro HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Cuatro.png",
    "Telecinco HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Telecinco.png",
    "Be Mad": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Be%20Mad.png",
    # Canales LaLiga
    "M+ LaLiga TV UHD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20LaLiga%20TV%20UHD.png",
    "M+ LaLiga TV HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20LaLiga%20TV.png",
    "M+ LaLiga TV 2 1080": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20LaLiga%20TV%202.png",
    "M+ LaLiga TV 2 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20LaLiga%20TV%202.png",
    "M+ LaLiga TV 3 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20LaLiga%20TV%203.png",
    "LaLiga TV BAR HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/LaLiga%20TV%20BAR%20HD.png",
    "DAZN LaLiga HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/DAZN%20LaLiga.png",
    "DAZN LaLiga HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/DAZN%20LaLiga.png",
    "DAZN LaLiga 2 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/DAZN%20LaLiga%202.png",
    # Canales LaLiga Hypermotion
    "LaLiga TV Hypermotion HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/LaLiga%20TV%20Hypermotion.png",
    "LaLiga TV Hypermotion 2": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/LaLiga%20TV%20Hypermotion%202.png",
    "LaLiga TV Hypermotion 3": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/LaLiga%20TV%20Hypermotion%203.png",
    # Canales Champions League
    "M+ Liga de Campeones HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones.png",
    "M+ Liga de Campeones 2 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%202.png",
    "M+ Liga de Campeones 3 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%203.png",
    "M+ Liga de Campeones 4": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%204.png",
    "M+ Liga de Campeones 5": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%205.png",
    "M+ Liga de Campeones 6": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%206.png",
    "M+ Liga de Campeones 7": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%207.png",
    "M+ Liga de Campeones 8": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%208.png",
    "M+ Liga de Campeones 9": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%209.png",
    "M+ Liga de Campeones 10": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%2010.png",
    "M+ Liga de Campeones 11": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%2011.png",
    "M+ Liga de Campeones 12": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%2012.png",
    "M+ Liga de Campeones 13": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Liga%20de%20Campeones%2013.png",
    # Canales Fórmula 1
    "DAZN F1 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/DAZN%20F1.png",
    # Canales Golf
    "M+ Golf HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Golf.png",
    "M+ Golf 2 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Golf%202.png",
    # Canales Eurosport
    "Eurosport 1 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Eurosport%201.png",
    "Eurosport 2 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Eurosport%202.png",
    # Otros canales
    "Movistar Plus+ HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Movistar%20Plus%2B.png",
    "M+ Deportes HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Deportes.png",
    "M+ Deportes 2 HD": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Deportes%202.png",
    "M+ Deportes 3": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Deportes%203.png",
    "M+ Deportes 4": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Deportes%204.png",
    "M+ Deportes 5": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Deportes%205.png",
    "M+ Deportes 6": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Deportes%206.png",
    "M+ Deportes 7": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Deportes%207.png",
    "Barcelona TV": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Barcelona%20TV.png",
    "Real Madrid TV": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/Real%20Madrid%20TV.png",
    "Onetoro": "https://onetoro.tv/assets/images/mundotoro-streaming-logo1.png",
}

MAPEO_LOGOS_POR_GRUPO = {
    "1-La Liga": "https://estatico.emisiondof6.com/recorte/m-NEONEGR/canal/MLIGA",
    "2-Liga Hypermotion": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/LaLiga%20TV%20Hypermotion%20HD.png",
    "3-Champions League": "https://estatico.emisiondof6.com/recorte/m-NEONEGR/canal/CHAPIO",
    "4-Fórmula 1": "https://estatico.emisiondof6.com/recorte/m-NEONEGR/canal/MVF1",
    "Satélite": "",
    "América": "",
    "Vamos": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Vamos%20HD.png",
    "Golf": "https://raw.githubusercontent.com/davidmuma/picons_dobleM/master/icon/M%2B%20Golf%20HD.png",
    "Tenis": "https://telegra.ph/file/8807aa3ba9ca7f2232492.jpg",
    "Sports": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTT-R_-LLcIAi3FM4uR_yMHX_jNGAasmCj4jQ&usqp=CAU",
    "Otros": ""
}



class CrawlerSpider(scrapy.Spider):
    name = "crawler"

    def start_requests(self):
        urls = [
            "https://elcano.top/",
            #"https://www.robertofreijo.com/acestream-ids/"
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_elcano, errback=self.fallback_request, meta={"url_secundaria": "https://www.robertofreijo.com/acestream-ids/"})

    def parse_elcano(self, response):
        with open("../lista.m3u", "w", encoding="utf-8") as f:
            #Cabecera archivo
            f.write('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_dobleM/master/guiatv.xml"\n')

            enlaces_a = response.css('a[href^="acestream://"]')

            if enlaces_a:
                # Iteramos por los enlaces acestream
                for a in enlaces_a:
                    nombre_original = (
                        a.css('::text').get().strip().replace('•', '').replace(':', '').strip()
                    )

                    if nombre_original == "" or nombre_original == "aquí": continue

                     # Unificar el nombre usando MAPEO_NOMBRES
                    nombre_unificado = MAPEO_NOMBRES_ELCANO.get(nombre_original, nombre_original)

                    # Obtener el ID del canal a partir del nombre unificado
                    tvg_id = MAPEO_IDS.get(nombre_unificado, nombre_unificado)

                    enlace = a.attrib['href'].replace('acestream://', '')  # Limpiamos el enlace

                    # Asignamos la categoría según el nombre del canal
                    group_title = self.get_group_title(nombre_unificado)
                    logo_url = MAPEO_LOGOS.get(tvg_id, MAPEO_LOGOS_POR_GRUPO.get(group_title, ""))

                    # Formato m3u con todos los atributos necesarios
                    entrada = (
                        f'\n#EXTINF:-1 group-title="{group_title}" tvg-id="{tvg_id}" tvg-name="{nombre_unificado}" tvg-logo="{logo_url}" ,{nombre_unificado}\n'
                        f'plugin://script.module.horus?action=play&id={enlace}\n'
                    )

                    # Escribimos la entrada en el archivo
                    f.write(entrada)
            else:
                self.log("No se encontraron enlaces => Explorando URL secundaria")
                url_secundaria = response.meta.get("url_secundaria")
                yield scrapy.Request(url=url_secundaria, callback=self.parse_robertofreijo, errback=self.handle_error)

    def fallback_request(self, failure):
        """Se ejecuta si la primera URL falla y lanza la segunda URL."""
        self.log(f"La primera URL falló: {failure.request.url}. Intentando la segunda URL...")

        # Lanza la segunda solicitud si la primera falla
        url_secundaria = failure.request.meta["url_secundaria"]
        yield scrapy.Request(url=url_secundaria, callback=self.parse_robertofreijo, errback=self.handle_error)


    def parse_robertofreijo(self, response):
        with open("../lista.m3u", "w", encoding="utf-8") as f:
            
            f.write('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_dobleM/master/guiatv.xml"\n') # Cabecera del archivo

            # Iteramos por los párrafos que contienen enlaces acestream
            for p in response.css('p'):
                nombre_original = (
                    p.css('::text').get().strip().replace('•', '').replace(':', '').strip()
                )

                if nombre_original == "" or nombre_original == "aquí": continue

                # Unificar el nombre usando MAPEO_NOMBRES
                nombre_unificado = MAPEO_NOMBRES_ROBERTOFREIJO.get(nombre_original, nombre_original)

                # Obtener el ID del canal a partir del nombre unificado
                tvg_id = MAPEO_IDS.get(nombre_unificado, nombre_unificado)
                
                enlace = p.css('a::attr(href)').get()

                # Verificamos si el enlace es válido
                if enlace and "acestream://" in enlace:
                    enlace = enlace.replace('acestream://', '')  # Limpiamos el enlace

                    # Asignamos la categoría según el nombre del canal
                    group_title = self.get_group_title(nombre_unificado)
                    logo_url = MAPEO_LOGOS.get(tvg_id, MAPEO_LOGOS_POR_GRUPO.get(group_title, ""))

                    # Formato m3u
                    entrada = (
                        f'\n#EXTINF:-1 group-title="{group_title}" tvg-id="{tvg_id}" tvg-name="{nombre_unificado}" tvg-logo="{logo_url}" ,{nombre_unificado}\n'
                        f'plugin://script.module.horus?action=play&id={enlace}\n'
                    )

                    # Escribimos la entrada en el archivo
                    f.write(entrada)

    def handle_error(self, failure):
        """Manejo de errores en la solicitud."""
        self.log(f"Error al procesar: {failure.request.url}", level=scrapy.log.ERROR)

    def get_group_title(self, nombre):
        """Clasifica los canales según su nombre."""
        nombre_lower = nombre.lower()  # Para comparación sin importar mayúsculas

        if "hypermotion" in nombre_lower or "smartbank" in nombre_lower:
            return "2-Liga Hypermotion"
        elif "campeones" in nombre_lower:
            return "3-Champions League"
        elif any(kw in nombre_lower for kw in ["liga", "laliga", "la liga"]):
            return "1-La Liga"
        elif "f1" in nombre_lower in nombre_lower:
            return "4-Fórmula 1"
        elif any(kw in nombre_lower for kw in ["la 1", "la1", "la 2", "la2", "telecinco", "antena", "cuatro", "teledeporte", "gol play", "be mad", "bemad"]):
            return "Satélite"
        elif "copa" in nombre_lower or "ppvp" in nombre_lower:
            return "América"
        elif "#" in nombre_lower:
            return "Vamos"
        elif "golf" in nombre_lower:
            return "Golf"
        elif "tenis" in nombre_lower or "tennis" in nombre_lower or "wimbledon" in nombre_lower:
            return "Tenis"
        elif "eurosport" in nombre_lower or "sport tv" in nombre_lower or "bein" in nombre_lower:
            return "Sports"
        else:
            return "Otros"  # Categoría residual
