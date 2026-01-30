from pydantic import BaseModel, computed_field, Field

class Booking(BaseModel) :
    user_id : int
    room_id : int
    nights : int = Field(..., ge=1)
    rate_per_night : float

    @computed_field
    @property
    def total_price(self) -> float : 
        return self.rate_per_night * self.nights
    

booking = Booking(
    user_id= 123,
    room_id=1234,
    nights=2,
    rate_per_night=100.0
)

print(booking.total_price)
print(booking.model_dump())