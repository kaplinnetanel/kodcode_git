# import logging 

# logging.basicConfig(
#     level=logging.DEBUG,                                    
#     filename="log.py",                                     
#     format="%(asctime)s | %(levelname)s | %(message)s")

# logger = logging.getLogger(__name__)
# #6
# def process_payment(user_id, amount):
#     logger.info(f'Starting payment for user {user_id}')
#     if amount <= 0:
#         logger.error('ERROR: Invalid amount')
#         return
#     if amount > 10000:
#         logger.warning('WARNING: Large transaction')
#     logger.info(f'Payment of {amount} completed for user {user_id}')

# #7
# logger = logging.getLogger("payments")
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler("app.log", encoding="utf-8")
# formatter = logging.ForSmatter(
#     "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
# )
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
#8

# logger = logging.getLogger(__name__)

# def read_config(filepath):
#     logger.debug(f" {filepath}")
    
#     try:
#         with open(filepath) as f:
#             data = f.read()
        
#         logger.info(f"{filepath}")
#         return data
        
#     except FileNotFoundError:
#         logger.exception(f"{filepath}")
#         return None