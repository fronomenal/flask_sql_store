from app.server import server, render_template, Item, request, current_user, flash, db
from app.utils.forms import PurchaseItemForm, PostItemForm

@server.route("/catalog", methods=["GET", "POST"])
def catalog():
    purchase_form = PurchaseItemForm()
    postitem_form = PostItemForm()

    if request.method == "POST":

        if request.form.get("_method"):
            pass

        item = int(request.form.get("purchased_item"))
        item_obj = Item.query.get(item)

        if item_obj and current_user.usrbudget >= item_obj.price:
            if not(item_obj.owner == current_user.id): 
                item_obj.owner = current_user.id
                current_user.usrbudget - item_obj.price;
            db.session.commit()

            flash("Item purchased successfully", category="success")
            return render_template("catalog.html", items=Item.query.all(), purchase_form=purchase_form)

        flash("Item not available or insufficient funds", category="danger")
        return render_template("catalog.html", Item.query.filter(Item.owner != current_user.id).all(), purchase_form=purchase_form)

    if request.method == "GET":
        if current_user.is_authenticated: 
            items = Item.query.filter(Item.owner != current_user.id).all()
        else:
            items=Item.query.all()


        return render_template("catalog.html", items=items, purchase_form=purchase_form, owned_items=None, postitem_form=postitem_form)