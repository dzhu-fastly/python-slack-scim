# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = users_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class UsersEmail:
    primary: Optional[bool]
    value: Optional[str]

    def __init__(self, primary: Optional[bool], value: Optional[str]) -> None:
        self.primary = primary
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'UsersEmail':
        assert isinstance(obj, dict)
        primary = from_union([from_bool, from_none], obj.get("primary"))
        value = from_union([from_str, from_none], obj.get("value"))
        return UsersEmail(primary, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["primary"] = from_union([from_bool, from_none], self.primary)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


class Meta:
    created: Optional[str]
    location: Optional[str]

    def __init__(self, created: Optional[str], location: Optional[str]) -> None:
        self.created = created
        self.location = location

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        created = from_union([from_str, from_none], obj.get("created"))
        location = from_union([from_str, from_none], obj.get("location"))
        return Meta(created, location)

    def to_dict(self) -> dict:
        result: dict = {}
        result["created"] = from_union([from_str, from_none], self.created)
        result["location"] = from_union([from_str, from_none], self.location)
        return result


class Name:
    family_name: Optional[str]
    given_name: Optional[str]

    def __init__(self, family_name: Optional[str], given_name: Optional[str]) -> None:
        self.family_name = family_name
        self.given_name = given_name

    @staticmethod
    def from_dict(obj: Any) -> 'Name':
        assert isinstance(obj, dict)
        family_name = from_union([from_str, from_none], obj.get("familyName"))
        given_name = from_union([from_str, from_none], obj.get("givenName"))
        return Name(family_name, given_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["familyName"] = from_union([from_str, from_none], self.family_name)
        result["givenName"] = from_union([from_str, from_none], self.given_name)
        return result


class Photo:
    type: Optional[str]
    value: Optional[str]

    def __init__(self, type: Optional[str], value: Optional[str]) -> None:
        self.type = type
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'Photo':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        return Photo(type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


class Address:
    country: Optional[str]
    locality: Optional[str]
    postal_code: Optional[str]
    primary: Optional[bool]
    region: Optional[str]
    street_address: Optional[str]

    def __init__(self, country: Optional[str], locality: Optional[str], postal_code: Optional[str], primary: Optional[bool], region: Optional[str], street_address: Optional[str]) -> None:
        self.country = country
        self.locality = locality
        self.postal_code = postal_code
        self.primary = primary
        self.region = region
        self.street_address = street_address

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        country = from_union([from_str, from_none], obj.get("country"))
        locality = from_union([from_str, from_none], obj.get("locality"))
        postal_code = from_union([from_str, from_none], obj.get("postalCode"))
        primary = from_union([from_bool, from_none], obj.get("primary"))
        region = from_union([from_str, from_none], obj.get("region"))
        street_address = from_union([from_str, from_none], obj.get("streetAddress"))
        return Address(country, locality, postal_code, primary, region, street_address)

    def to_dict(self) -> dict:
        result: dict = {}
        result["country"] = from_union([from_str, from_none], self.country)
        result["locality"] = from_union([from_str, from_none], self.locality)
        result["postalCode"] = from_union([from_str, from_none], self.postal_code)
        result["primary"] = from_union([from_bool, from_none], self.primary)
        result["region"] = from_union([from_str, from_none], self.region)
        result["streetAddress"] = from_union([from_str, from_none], self.street_address)
        return result


class PhoneNumberElement:
    primary: Optional[bool]
    type: Optional[str]
    value: Optional[str]

    def __init__(self, primary: Optional[bool], type: Optional[str], value: Optional[str]) -> None:
        self.primary = primary
        self.type = type
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'PhoneNumberElement':
        assert isinstance(obj, dict)
        primary = from_union([from_bool, from_none], obj.get("primary"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        return PhoneNumberElement(primary, type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["primary"] = from_union([from_bool, from_none], self.primary)
        result["type"] = from_union([from_str, from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


class Group:
    display: Optional[str]
    value: Optional[str]

    def __init__(self, display: Optional[str], value: Optional[str]) -> None:
        self.display = display
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        assert isinstance(obj, dict)
        display = from_union([from_str, from_none], obj.get("display"))
        value = from_union([from_str, from_none], obj.get("value"))
        return Group(display, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["display"] = from_union([from_str, from_none], self.display)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


class Manager:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'Manager':
        assert isinstance(obj, dict)
        return Manager()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class UrnScimSchemasExtensionEnterprise10:
    manager: Optional[Manager]

    def __init__(self, manager: Optional[Manager]) -> None:
        self.manager = manager

    @staticmethod
    def from_dict(obj: Any) -> 'UrnScimSchemasExtensionEnterprise10':
        assert isinstance(obj, dict)
        manager = from_union([Manager.from_dict, from_none], obj.get("manager"))
        return UrnScimSchemasExtensionEnterprise10(manager)

    def to_dict(self) -> dict:
        result: dict = {}
        result["manager"] = from_union([lambda x: to_class(Manager, x), from_none], self.manager)
        return result


class Resource:
    active: Optional[bool]
    addresses: Optional[List[Address]]
    display_name: Optional[str]
    emails: Optional[List[PhoneNumberElement]]
    external_id: Optional[str]
    groups: Optional[List[Group]]
    id: Optional[str]
    meta: Optional[Meta]
    name: Optional[Name]
    nick_name: Optional[str]
    phone_numbers: Optional[List[PhoneNumberElement]]
    photos: Optional[List[Photo]]
    profile_url: Optional[str]
    roles: Optional[List[PhoneNumberElement]]
    schemas: Optional[List[str]]
    timezone: Optional[str]
    title: Optional[str]
    urn_scim_schemas_extension_enterprise_10: Optional[UrnScimSchemasExtensionEnterprise10]
    user_name: Optional[str]

    def __init__(self, active: Optional[bool], addresses: Optional[List[Address]], display_name: Optional[str], emails: Optional[List[PhoneNumberElement]], external_id: Optional[str], groups: Optional[List[Group]], id: Optional[str], meta: Optional[Meta], name: Optional[Name], nick_name: Optional[str], phone_numbers: Optional[List[PhoneNumberElement]], photos: Optional[List[Photo]], profile_url: Optional[str], roles: Optional[List[PhoneNumberElement]], schemas: Optional[List[str]], timezone: Optional[str], title: Optional[str], urn_scim_schemas_extension_enterprise_10: Optional[UrnScimSchemasExtensionEnterprise10], user_name: Optional[str]) -> None:
        self.active = active
        self.addresses = addresses
        self.display_name = display_name
        self.emails = emails
        self.external_id = external_id
        self.groups = groups
        self.id = id
        self.meta = meta
        self.name = name
        self.nick_name = nick_name
        self.phone_numbers = phone_numbers
        self.photos = photos
        self.profile_url = profile_url
        self.roles = roles
        self.schemas = schemas
        self.timezone = timezone
        self.title = title
        self.urn_scim_schemas_extension_enterprise_10 = urn_scim_schemas_extension_enterprise_10
        self.user_name = user_name

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        active = from_union([from_bool, from_none], obj.get("active"))
        addresses = from_union([lambda x: from_list(Address.from_dict, x), from_none], obj.get("addresses"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        emails = from_union([lambda x: from_list(PhoneNumberElement.from_dict, x), from_none], obj.get("emails"))
        external_id = from_union([from_str, from_none], obj.get("externalId"))
        groups = from_union([lambda x: from_list(Group.from_dict, x), from_none], obj.get("groups"))
        id = from_union([from_str, from_none], obj.get("id"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        name = from_union([Name.from_dict, from_none], obj.get("name"))
        nick_name = from_union([from_str, from_none], obj.get("nickName"))
        phone_numbers = from_union([lambda x: from_list(PhoneNumberElement.from_dict, x), from_none], obj.get("phoneNumbers"))
        photos = from_union([lambda x: from_list(Photo.from_dict, x), from_none], obj.get("photos"))
        profile_url = from_union([from_str, from_none], obj.get("profileUrl"))
        roles = from_union([lambda x: from_list(PhoneNumberElement.from_dict, x), from_none], obj.get("roles"))
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        timezone = from_union([from_str, from_none], obj.get("timezone"))
        title = from_union([from_str, from_none], obj.get("title"))
        urn_scim_schemas_extension_enterprise_10 = from_union([UrnScimSchemasExtensionEnterprise10.from_dict, from_none], obj.get("urn:scim:schemas:extension:enterprise:1.0"))
        user_name = from_union([from_str, from_none], obj.get("userName"))
        return Resource(active, addresses, display_name, emails, external_id, groups, id, meta, name, nick_name, phone_numbers, photos, profile_url, roles, schemas, timezone, title, urn_scim_schemas_extension_enterprise_10, user_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["active"] = from_union([from_bool, from_none], self.active)
        result["addresses"] = from_union([lambda x: from_list(lambda x: to_class(Address, x), x), from_none], self.addresses)
        result["displayName"] = from_union([from_str, from_none], self.display_name)
        result["emails"] = from_union([lambda x: from_list(lambda x: to_class(PhoneNumberElement, x), x), from_none], self.emails)
        result["externalId"] = from_union([from_str, from_none], self.external_id)
        result["groups"] = from_union([lambda x: from_list(lambda x: to_class(Group, x), x), from_none], self.groups)
        result["id"] = from_union([from_str, from_none], self.id)
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["name"] = from_union([lambda x: to_class(Name, x), from_none], self.name)
        result["nickName"] = from_union([from_str, from_none], self.nick_name)
        result["phoneNumbers"] = from_union([lambda x: from_list(lambda x: to_class(PhoneNumberElement, x), x), from_none], self.phone_numbers)
        result["photos"] = from_union([lambda x: from_list(lambda x: to_class(Photo, x), x), from_none], self.photos)
        result["profileUrl"] = from_union([from_str, from_none], self.profile_url)
        result["roles"] = from_union([lambda x: from_list(lambda x: to_class(PhoneNumberElement, x), x), from_none], self.roles)
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["timezone"] = from_union([from_str, from_none], self.timezone)
        result["title"] = from_union([from_str, from_none], self.title)
        result["urn:scim:schemas:extension:enterprise:1.0"] = from_union([lambda x: to_class(UrnScimSchemasExtensionEnterprise10, x), from_none], self.urn_scim_schemas_extension_enterprise_10)
        result["userName"] = from_union([from_str, from_none], self.user_name)
        return result


class Users:
    active: Optional[bool]
    display_name: Optional[str]
    emails: Optional[List[UsersEmail]]
    external_id: Optional[str]
    groups: Optional[List[str]]
    id: Optional[str]
    items_per_page: Optional[int]
    meta: Optional[Meta]
    name: Optional[Name]
    nick_name: Optional[str]
    photos: Optional[List[Photo]]
    profile_url: Optional[str]
    resources: Optional[List[Resource]]
    schemas: Optional[List[str]]
    start_index: Optional[int]
    timezone: Optional[str]
    title: Optional[str]
    total_results: Optional[int]
    user_name: Optional[str]

    def __init__(self, active: Optional[bool], display_name: Optional[str], emails: Optional[List[UsersEmail]], external_id: Optional[str], groups: Optional[List[str]], id: Optional[str], items_per_page: Optional[int], meta: Optional[Meta], name: Optional[Name], nick_name: Optional[str], photos: Optional[List[Photo]], profile_url: Optional[str], resources: Optional[List[Resource]], schemas: Optional[List[str]], start_index: Optional[int], timezone: Optional[str], title: Optional[str], total_results: Optional[int], user_name: Optional[str]) -> None:
        self.active = active
        self.display_name = display_name
        self.emails = emails
        self.external_id = external_id
        self.groups = groups
        self.id = id
        self.items_per_page = items_per_page
        self.meta = meta
        self.name = name
        self.nick_name = nick_name
        self.photos = photos
        self.profile_url = profile_url
        self.resources = resources
        self.schemas = schemas
        self.start_index = start_index
        self.timezone = timezone
        self.title = title
        self.total_results = total_results
        self.user_name = user_name

    @staticmethod
    def from_dict(obj: Any) -> 'Users':
        assert isinstance(obj, dict)
        active = from_union([from_bool, from_none], obj.get("active"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        emails = from_union([lambda x: from_list(UsersEmail.from_dict, x), from_none], obj.get("emails"))
        external_id = from_union([from_str, from_none], obj.get("externalId"))
        groups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("groups"))
        id = from_union([from_str, from_none], obj.get("id"))
        items_per_page = from_union([from_int, from_none], obj.get("itemsPerPage"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        name = from_union([Name.from_dict, from_none], obj.get("name"))
        nick_name = from_union([from_str, from_none], obj.get("nickName"))
        photos = from_union([lambda x: from_list(Photo.from_dict, x), from_none], obj.get("photos"))
        profile_url = from_union([from_str, from_none], obj.get("profileUrl"))
        resources = from_union([lambda x: from_list(Resource.from_dict, x), from_none], obj.get("Resources"))
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        start_index = from_union([from_int, from_none], obj.get("startIndex"))
        timezone = from_union([from_str, from_none], obj.get("timezone"))
        title = from_union([from_str, from_none], obj.get("title"))
        total_results = from_union([from_int, from_none], obj.get("totalResults"))
        user_name = from_union([from_str, from_none], obj.get("userName"))
        return Users(active, display_name, emails, external_id, groups, id, items_per_page, meta, name, nick_name, photos, profile_url, resources, schemas, start_index, timezone, title, total_results, user_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["active"] = from_union([from_bool, from_none], self.active)
        result["displayName"] = from_union([from_str, from_none], self.display_name)
        result["emails"] = from_union([lambda x: from_list(lambda x: to_class(UsersEmail, x), x), from_none], self.emails)
        result["externalId"] = from_union([from_str, from_none], self.external_id)
        result["groups"] = from_union([lambda x: from_list(from_str, x), from_none], self.groups)
        result["id"] = from_union([from_str, from_none], self.id)
        result["itemsPerPage"] = from_union([from_int, from_none], self.items_per_page)
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["name"] = from_union([lambda x: to_class(Name, x), from_none], self.name)
        result["nickName"] = from_union([from_str, from_none], self.nick_name)
        result["photos"] = from_union([lambda x: from_list(lambda x: to_class(Photo, x), x), from_none], self.photos)
        result["profileUrl"] = from_union([from_str, from_none], self.profile_url)
        result["Resources"] = from_union([lambda x: from_list(lambda x: to_class(Resource, x), x), from_none], self.resources)
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["startIndex"] = from_union([from_int, from_none], self.start_index)
        result["timezone"] = from_union([from_str, from_none], self.timezone)
        result["title"] = from_union([from_str, from_none], self.title)
        result["totalResults"] = from_union([from_int, from_none], self.total_results)
        result["userName"] = from_union([from_str, from_none], self.user_name)
        return result


def users_from_dict(s: Any) -> Users:
    return Users.from_dict(s)


def users_to_dict(x: Users) -> Any:
    return to_class(Users, x)
