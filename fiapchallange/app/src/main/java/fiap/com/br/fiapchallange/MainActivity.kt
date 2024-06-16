package fiap.com.br.fiapchallange

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.text.Editable
import android.text.SpannableStringBuilder
import android.text.TextWatcher
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import com.pchmn.materialchips.ChipView
import com.pchmn.materialchips.ChipsInput
import com.pchmn.materialchips.model.ChipInterface
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.content_main.*
import fiap.com.br.fiapchallange.data.Database
import fiap.com.br.fiapchallange.domain.User
import fiap.com.br.fiapchallange.util.*

class MainActivity :
        AppCompatActivity(),
        ChipsInput.ChipsListener,
        TextWatcher {

    var hasTag: Boolean = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        et_message.addTextChangedListener(this)

        ci_contacts.addChipsListener( this )
        ci_contacts.setFilterableList( Database.getContacts(this) )


    }

    override fun onResume() {
        super.onResume()
        toolbar.setNavigationIcon(R.drawable.ic_account_plus_white_24dp)
        toolbar.setTitle("Email social para quem?")
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }




    override fun onTextChanged(contact: CharSequence?) {
        if( isEmail( contact.toString() ) ){
            ci_contacts.addChip( getUserByEmail( contact.toString() ) )
        }
    }
    override fun onChipAdded(user: ChipInterface?, p1: Int) {}
    override fun onChipRemoved(user: ChipInterface?, p1: Int) {}


    private fun getUserByEmail(contact: String): ChipInterface {

        val email = contact.substring(0, contact.length - 1)

        for( user in ci_contacts.filterableList ){
            if( user.info.equals(email, true) ){
                return user
            }
        }

        return User(
                this,
                null,
                email.split("@")[0],
                email
        )
    }


    override fun onTextChanged(text: CharSequence?, p1: Int, p2: Int, p3: Int) {
        if( containsHashTag( text.toString() ) ){

            hasTag = true
        }
        else if( hasTag ){
            hasTag = false
            changeHashTagToImage( text.toString() )
        }

    }
    override fun afterTextChanged(p0: Editable?) {}
    override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {}

    private fun changeHashTagToImage(text: String){
        val match = getHashTagMatch(text)

        while( match.find() ) {
            val hashTag = match.group()
            val beginPosition = text.indexOf(hashTag)
            val startPosition = text.indexOf(hashTag) + hashTag.length

            val chipView = ChipView(this)
            chipView.label = hashTag.replace("#", "")
            val imgBitmap = createBitmapFromView( chipView )


            var spannable = et_message.text as SpannableStringBuilder
            spannable = retrieveSpannableWithBitmap(
                this,
                spannable,
                imgBitmap,
                beginPosition,
                startPosition )

            et_message.setText( spannable )
            et_message.setSelection( spannable.length ) /* Para manter o cursor no final do text no EditText. */
        }
    }
}
