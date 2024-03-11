from fastapi import HTTPException, status

# Создание собственных исключений (exceptions) было изменено
# на предпочтительный подход. 


class AccountException(HTTPException):
    status_code = 500
    detail = ""
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(AccountException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"
        
class IncorrectEmailOrPasswordException(AccountException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверная почта или пароль"
        
class TokenExpiredException(AccountException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Срок действия токена истек"
        
class TokenAbsentException(AccountException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"
        
class IncorrectTokenFormatException(AccountException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"
        
class UserIsNotPresentException(AccountException):
    status_code=status.HTTP_401_UNAUTHORIZED

class RoomFullyBooked(AccountException):
    status_code=status.HTTP_409_CONFLICT
    detail="Не осталось свободных счетов"

class RoomCannotBeBooked(AccountException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось забронировать номер ввиду неизвестной ошибки"

class DateFromCannotBeAfterDateTo(AccountException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Дата заезда не может быть позже даты выезда"



class CannotAddDataToDatabase(AccountException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось добавить запись"

