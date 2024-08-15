from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLElementProps
    from ..types import ChildType

class Fragment(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLElementProps"]):
        super().__init__(*children, **kwargs)

    tag_name = "fragment"
