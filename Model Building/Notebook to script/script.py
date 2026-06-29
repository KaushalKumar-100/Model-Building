import logging

logging.basicConfig(
    level=logging.DEBUG, #debug will print both debug and info
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  #terminal
        logging.FileHandler("app.log")  #file
        
    ]
)
logging.info("Program started")
logging.debug("Debugging code")
logging.warning("This is a Warning")
logging.error("This is an error")









    

