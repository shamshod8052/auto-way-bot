from aiogram.fsm.state import StatesGroup, State


class GetForm(StatesGroup):
    QUESTION = State()
    OFFER_TYPE = State()
    OFFER = State()
    SUPPORT_TYPE = State()
    SUPPORT = State()
    GET_USER_ID = State()
    ANSWER = State()
