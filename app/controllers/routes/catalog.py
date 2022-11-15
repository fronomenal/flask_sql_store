from app.server import server, render_template, Item, request, current_user, flash, db, redirect, url_for, Item
from app.utils.forms import PurchaseItemForm, PostItemForm, PriceChangeForm

@server.route("/catalog", methods=["GET", "POST"])
def catalog():
    purchase_form = PurchaseItemForm()
    postitem_form = PostItemForm()
    price_form = PriceChangeForm();

    if request.method == "POST":

        if request.form.get("_method") == "patch":
            if price_form.validate_on_submit():
                item = int(request.form.get("changed_item"))
                item_obj = Item.query.get(item)
                if current_user.id == item_obj.owner: 
                    item_obj.price = price_form.price.data
                    db.session.commit()


                flash("Price changed successfully", category="success")
                return redirect(url_for("catalog"))

        if request.form.get("_method") == "put":
            if postitem_form.validate_on_submit():
                newitem = Item(name=postitem_form.itmname.data, price=postitem_form.price.data, barcode=postitem_form.barcode.data, description=postitem_form.description.data, owner=current_user.id)
                db.session.add(newitem)
                db.session.commit()

                flash("Item added successfully", category="success")
                return redirect(url_for("catalog"))

        item = int(request.form.get("purchased_item"))
        item_obj = Item.query.get(item)

        if item_obj and current_user.usrbudget >= item_obj.price:
            if not(item_obj.owner == current_user.id): 
                item_obj.owner = current_user.id
                current_user.usrbudget - item_obj.price;
            db.session.commit()

            flash("Item purchased successfully", category="success")
            return redirect(url_for("catalog"))

        flash("Item not available or insufficient funds", category="danger")
        return redirect(url_for("catalog"))

    if request.method == "GET":
        if current_user.is_authenticated: 
            items = Item.query.filter(Item.owner != current_user.id).all()
            owned_items=Item.query.filter_by(owner=current_user.id).all()
        else:
            items=Item.query.all()
            owned_items=None


        return render_template("catalog.html", items=items, purchase_form=purchase_form, owned_items=owned_items, postitem_form=postitem_form, price_form=price_form)