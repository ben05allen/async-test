from sqlalchemy.ext.asyncio import AsyncSession

import schedules
from models.user import User, Company, Address, Geo


async def add_user(user: schedules.User, session: AsyncSession):
    new_user = User(
        id=user.id,
        name=user.name,
        username=user.username,
        email=user.email,
        phone=user.phone,
        website=user.website,
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    new_company = Company(
        user_id=user.id,
        name=user.company.name,
        catchPhrase=user.company.catchPhrase,
        bs=user.company.bs,
    )
    session.add(new_company)
    await session.commit()

    new_address = Address(
        user_id=user.id,
        street=user.address.street,
        suite=user.address.suite,
        city=user.address.city,
        zipcode=user.address.zipcode,
    )
    session.add(new_address)
    await session.commit()
    await session.refresh(new_address)

    new_geo = Geo(
        address_id=new_address.id,
        lat=user.address.geo.lat,
        lng=user.address.geo.lng,
    )
    session.add(new_geo)
    await session.commit()
